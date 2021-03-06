const std = @import("std");
const Builder = std.build.Builder;

pub fn build(b: *Builder) void {
    const mode = b.standardReleaseOptions();
    const lib = b.addStaticLibrary("zig", "src/zigfactorial.zig");

    // Need these flags in order to compile
    lib.bundle_compiler_rt = true;
    lib.force_pic = true;
    lib.single_threaded = true;
    lib.strip = true;

    lib.setBuildMode(mode);
    lib.install();

    var main_tests = b.addTest("src/zigfactorial.zig");
    main_tests.setBuildMode(mode);

    const test_step = b.step("test", "Run library tests");
    test_step.dependOn(&main_tests.step);
}
