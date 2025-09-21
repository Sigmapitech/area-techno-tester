{
  description = "Flutter environment (no Android, no Web)";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachSystem [ "x86_64-linux" ] (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          config.allowUnfree = true;
        };
      in
      {
        devShell = with pkgs; mkShell rec {
          JAVA_HOME = jdk17.home;
          FLUTTER_ROOT = flutter;
          DART_ROOT = "${flutter}/bin/cache/dart-sdk";

          buildInputs = [
            flutter
            gradle
            jdk17
            protobuf
            buf
            pandoc
            libsecret.dev
            gtk3.dev
            grpcurl
            pkg-config
          ];

          CMAKE_PREFIX_PATH = "${pkgs.lib.makeLibraryPath [libsecret.dev gtk3.dev]}";

          shellHook = ''
            if [ -z "$PUB_CACHE" ]; then
              export PATH="$PATH:$HOME/.pub-cache/bin"
            else
              export PATH="$PATH:$PUB_CACHE/bin"
            fi

            dart pub global activate protoc_plugin
          '';
        };
      }
    );
}