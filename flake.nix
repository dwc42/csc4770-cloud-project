{
  description = "pywebview-react-app";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-26.05";

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
      pythonEnv = pkgs.python3.withPackages (ps: with ps; [
        pyinstaller
        pywebview
        pyqt6
        pyqt6-webengine
      ]);
      qtEnv = pkgs.buildEnv {
        name = "qt-custom-${pkgs.qt6.qtbase.version}";
        paths = with pkgs.qt6; [
          qtbase
          qtwebengine
          # add more here
        ];
        pathsToLink = [
          "/bin" "/mkspecs" "/include" "/lib" "/share" "/libexec" "/metatypes"
          "/resources"
          "/qtwebengine_locales"
        ];
      };
      
      mkApp = yarnBuildScript: pkgs.callPackage ./package.nix {
        inherit pythonEnv qtEnv yarnBuildScript;
      };
    in {
      packages.${system} = rec {
        full = mkApp "build";
        backend = mkApp "backend";
        container = pkgs.dockerTools.buildImage {
          name = "pywebview-react-app";
          tag = "latest";
          copyToRoot = pkgs.buildEnv {
            name = "qq";
            paths = [ backend ];
            pathsToLink = [ "/bin" ];
          };
        };
        default = full;
      };
    };
}
