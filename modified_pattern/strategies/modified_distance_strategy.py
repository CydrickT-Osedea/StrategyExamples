from abc import ABC
from modified_pattern.modified_projectile import ModifiedProjectile

from modified_pattern.strategies.configurations.configuration import Configuration

class ModifiedDistanceStrategy(ABC):

    # This is used by whoever is going to call the strategy to give the configuration to the strategy.
    # Note that we're accepting the generic type `Configuration`, and not a specific implementation 
    # tailored to a specific strategy. The strategy will simply cast it to the type the strategy expects.
    def set_configuration(self, configuration: Configuration) -> None:
        self.configuration = configuration

    # This is used by the specific strategy's code to read the configuration. Again, note that the return type is `Configuration` and not a specific type of configuration. As mentioned above, the strategy will simply cast it to the type the strategy expects.
    def get_configuration(self) -> Configuration:
        return self.configuration
    
    # We give the whole projectile to the strategy. The strategy will call properties of the projectile (ie: the initial_velocity and the angle) to determine the distance.
    def get_distance(self, projectile: ModifiedProjectile) -> float:
        raise NotImplementedError()

    # Note that here we could add other getters for various resources. For instance, let's imagine that we would include the wind speed in our calculation. We could provide a method to ge the wind speed and direction here. The method would fetch from an external API the current wind speed and direction, and return it. The specific strategy's code would then call the method (like it does for `get_configuration()`) to get the wind speed and direction.