{
  outputs = { self }: let
    pkgs = import ../../nixpkgs.nix { system = "x86_64-linux";         config.allowUnfree = true;
        config.android_sdk.accept_license = true;};
  in {
    devShells.${pkgs.system} = {
      default = pkgs.mkShell {
      packages = with pkgs; [
        eslint
        nodejs
        typescript
        biome
        vite
        eas-cli
      ];
    };
      android = pkgs.mkShell {
        env = rec {
          ANDROID_SDK_ROOT = "${pkgs.androidenv.androidPkgs.androidsdk}/libexec/android-sdk";
          ANDROID_HOME = ANDROID_SDK_ROOT;
          PATH = "$ANDROID_HOME/emulator:$ANDROID_HOME/platform-tools:$ANDROID_HOME/cmdline-tools/latest/bin:$PATH";
        };
        packages = with pkgs; [
          android-studio-full
        ] ++ (with pkgs.androidenv.androidPkgs; [
          androidsdk
          emulator
        ]);
      };
    };
  };
}
