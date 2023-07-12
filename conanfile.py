from conan import ConanFile
from conan.tools.cmake import cmake_layout


class CompressorRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("glm/cci.20230113")
        self.requires("imgui/1.89.4")

        if self.settings.os != "Android":
            self.requires("boost/1.81.0")
            self.requires("libpng/1.6.39")
            
    def layout(self):
        if self.settings.os == "Android":
            cmake_layout(self)
