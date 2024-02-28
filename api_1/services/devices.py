
class Device:
    @classmethod
    def create_device_dictionary(cls, device_data: dict) -> dict:
        return {
            'device_type': device_data.get('device_type'),
            'host': device_data.get('host'),
            'username': device_data.get('username'),
            'password': device_data.get('password'),
        }
