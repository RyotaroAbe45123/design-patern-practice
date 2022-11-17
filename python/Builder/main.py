from salt_water.salt_water_builder import SaltWaterBuilder
from director import Director

def main():
    salt_water_builder = SaltWaterBuilder()
    director = Director(salt_water_builder)
    director.constract()
    print(director.get_result())

if __name__ == "__main__":
    main()