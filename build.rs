fn main() {
    let path = "./lib/go";
    let lib = "go_main";

    println!("cargo:rustc-link-search=native={}", path);
    println!("cargo:rustc-link-lib=static={}", lib);
}
