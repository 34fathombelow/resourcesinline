import random
import yaml

# Define possible values for cache configurations
cache_types = ["redis", "memcached", "in-memory", "filesystem"]
cache_sizes = ["128MB", "256MB", "512MB", "1GB", "2GB", "4GB"]

# Function to generate random cache configuration
def generate_random_cache_config(index):
    return {
        "name": f"cache-config-{index}",
        "data": {
            "cache_size": random.choice(cache_sizes),
            "cache_type": random.choice(cache_types)
        }
    }

# Generate 1000 random cache configurations
cache_configs = [generate_random_cache_config(i) for i in range(1, 1001)]

# Convert to YAML format with the desired structure
yaml_output = yaml.dump(cache_configs, default_flow_style=False)

# Write the output to a file
with open("random_cache_configs.yaml", "w") as file:
    file.write(yaml_output)

print("1000 random cache configurations generated and saved to 'random_cache_configs.yaml'.")
