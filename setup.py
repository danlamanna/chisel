from distutils.core import setup

setup(name="chisel",
      version="0.1",
      description="Chisel, Lightweight development environment management.",
      author="Dan LaManna",
      author_email="dan.lamanna@gmail.com",
      url="http://danlamanna.com",
      package_dir={ "chisel": "src/chisel" },
      packages=["chisel",
                "chisel.config"],
      provides=["chisel"],
      scripts=["scripts/chisel-add-db-replacement",
               "scripts/chisel-add-db",
               "scripts/chisel-checkout-project",
               "scripts/chisel-pull-db"])
