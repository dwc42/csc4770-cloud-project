{
  lib,
  stdenv,
  fetchFromGitHub,
  fetchYarnDeps,
  yarnConfigHook,
  yarnBuildHook,
  yarnInstallHook,
  
  pythonEnv,
  qtEnv,
  jq,
  nodejs,
  runCommand
}:
stdenv.mkDerivation (finalAttrs: rec {
  pname = "pywebview-react-app";
  version = "0.1.0";

  src = ./. ;

  yarnOfflineCache = fetchYarnDeps {
    yarnLock = finalAttrs.src + "/yarn.lock";
    hash = "sha256-P4TjWrGI/loGVQaXR8nZMl3Yspcaa7iD1UGxybzI4ao=";
  };

  patchedPackageJSON = runCommand "package.json"
	  {
	  	nativeBuildInputs = [ jq ];
	  }
	  # --onefile is not correct | un-venv the yarn scripts (using nix stuff)
	  ''
	    sed "s#build-linux\.spec --onefile#build-linux.spec#g" ${finalAttrs.src}/package.json | jq '
	      .scripts |= map_values(gsub("\\./venv-pywebview/bin/"; ""))
	      ' > $out
	  '';
  
  postPatch = ''
    cp ${patchedPackageJSON} ./package.json
  '';

  preBuild = ''
    export QT_ENV_PREFIX=${qtEnv}
    export NIX_BUILD=1
  '';

  postBuild = ''
    mkdir $out
  	mkdir $out/bin
  	mv dist/${pname}/* $out/bin
  	mv dist $out
  '';
  
  nativeBuildInputs = [
    yarnConfigHook
    yarnBuildHook
    yarnInstallHook
    # Needed for executing package.json scripts
    nodejs
    pythonEnv
    qtEnv
  ];

  # meta = {
    # ...
  # };
})