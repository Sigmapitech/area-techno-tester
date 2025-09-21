{
  outputs = { self }: let
    pkgs = import ../../nixpkgs.nix {
      system = "x86_64-linux";
      config.allowUnfree = true;
      config.android_sdk.accept_license = true;
    };
  in {
    devShells.${pkgs.system} = {
      default = with pkgs; pkgs.mkShell {
          JAVA_HOME = jdk17.home;
          FLUTTER_ROOT = flutter;
          DART_ROOT = "${flutter}/bin/cache/dart-sdk";

          packages = [
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
          ] ++ (with pkgs.androidenv.androidPkgs; [
            androidsdk
          ]);

          CMAKE_PREFIX_PATH = "${pkgs.lib.makeLibraryPath [libsecret.dev gtk3.dev]}";

          shellHook = ''
            if [ -z "$PUB_CACHE" ]; then
              export PATH="$PATH:$HOME/.pub-cache/bin"
            else
              export PATH="$PATH:$PUB_CACHE/bin"
            fi

            export JAVA_HOME=${pkgs.jdk17.home}
            export PATH="$JAVA_HOME/bin:$PATH"

            dart pub global activate protoc_plugin
          '';
        };
      android = pkgs.mkShell {
        inherit (self.devShells.${pkgs.system}) default;
        env = rec {
          ANDROID_SDK_ROOT = "${pkgs.androidenv.androidPkgs.androidsdk}/libexec/android-sdk";
          ANDROID_HOME = ANDROID_SDK_ROOT;
          PATH = "$ANDROID_HOME/emulator:$ANDROID_HOME/platform-tools:$ANDROID_HOME/cmdline-tools/latest/bin:$PATH";
        };
        packages = with pkgs; [
          android-studio-full
        ] ++ (with pkgs.androidenv.androidPkgs; [
          emulator
        ]);
      };
    };
  };
}
