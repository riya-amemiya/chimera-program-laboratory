fn main() {
    let paths = ["./lib/go", "./lib/zig/zig-out/lib"];
    let libs = ["go_main", "zig"];

    for path in paths.iter() {
        println!("cargo:rustc-link-search={}", path);
    }
    for libs in libs.iter() {
        println!("cargo:rustc-link-lib={}", libs);
    }
}
