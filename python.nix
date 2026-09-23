{
  lib,
  stdenv,
  fetchFromGitHub,
  makeWrapper,
  
  pythonEnv,
  runCommand
}: stdenv.mkDerivation (finalAttrs: rec {
  pname = "cli";
  version = "0.1.0";

  src = ./. ;

  # split this into the proper phases later maybe
  installPhase = ''
    runHook preInstall

    mkdir $out
    cp -r ./src $out/src
    mkdir $out/bin

    # prepend shebang so wrapper works
    echo -e "#!${ pythonEnv }/bin/python3\n" >> patched
    cat $out/src/backend/cli.py >> patched
    cp patched $out/src/backend/cli.py

    # wrap with pythonEnv
    chmod +x $out/src/backend/cli.py
    wrapProgram $out/src/backend/cli.py \
    	--prefix PATH ${ lib.makeBinPath [ pythonEnv ] }

    mv $out/src/backend/cli.py $out/bin/cli

    runHook postInstall
  '';

  nativeBuildInputs = [
    pythonEnv
    makeWrapper
  ];

  # meta = {
    # ...
  # };
})
