import configparser


config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getapplicationurl():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getemail():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getnewpassword():
        newpassword = config.get('common info', 'newpassword')
        return newpassword


    @staticmethod
    def get_package_device_1():
        package = config.get('device_1', 'package')
        return package


    @staticmethod
    def get_activity_device_1():
        activity = config.get('device_1', 'activity')
        return activity

    @staticmethod
    def get_platform_name_device_1():
        platform_name = config.get('device_1', 'platform_name')
        return platform_name

    @staticmethod
    def get_platform_version_device_1():
        platform_version = config.get('device_1', 'platform_version')
        return platform_version

    @staticmethod
    def get_device_name_device_1():
        device_name = config.get('device_1', 'device_name')
        return device_name

    @staticmethod
    def get_udid_device_1():
        udid = config.get('device_1', 'udid')
        return udid

    @staticmethod
    def get_automator_name_device_1():
        automator_name_device_1 = config.get('device_1', 'automator_name')
        return automator_name_device_1

    @staticmethod
    def get_port_device_1():
        port = config.get('device_1', 'port')
        return port

    @staticmethod
    def get_package_device_2():
        package = config.get('device_2', 'package')
        return package

    @staticmethod
    def get_activity_device_2():
        activity = config.get('device_2', 'activity')
        return activity

    @staticmethod
    def get_platform_name_device_2():
        platform_name = config.get('device_2', 'platform_name')
        return platform_name

    @staticmethod
    def get_platform_version_device_2():
        platform_version = config.get('device_2', 'platform_version')
        return platform_version

    @staticmethod
    def get_device_name_device_2():
        device_name = config.get('device_2', 'device_name')
        return device_name

    @staticmethod
    def get_udid_device_2():
        udid = config.get('device_2', 'udid')
        return udid

    @staticmethod
    def get_automator_name_device_2():
        automator_name_device_2 = config.get('device_2', 'automator_name')
        return automator_name_device_2

    @staticmethod
    def get_port_device_2():
        port = config.get('device_2', 'port')
        return port
