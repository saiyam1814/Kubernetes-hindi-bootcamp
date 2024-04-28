from kubernetes import client, config

def main():
    config.load_incluster_config()

    v1 = client.CoreV1Api()
    config_map_name = 'app-config'
    namespace = 'default'

    try:
        config_map = v1.read_namespaced_config_map(config_map_name, namespace)
        print("ConfigMap data:")
        for key, value in config_map.data.items():
            print(f"{key}: {value}")
    except client.exceptions.ApiException as e:
        print(f"Exception when calling CoreV1Api->read_namespaced_config_map: {e}")

if __name__ == '__main__':
    main()