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
    in {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = [
        	pythonEnv
        	qtEnv
        	pkgs.jq
        	pkgs.nodejs
        	pkgs.yarn
        ];
      };
      packages.${system}.default = pkgs.callPackage ./package.nix {
      	inherit pythonEnv qtEnv;
      };
    };
}