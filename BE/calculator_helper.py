import logger

class CalculatorHelper():
    log_properties = {
        'custom_dimensions': {
            'Ahmednur': 'Ahmednur_mahamud',
        }
    }
    
    _instance = None
    _is_initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculatorHelper, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            self._user_list = []
            self._current_user = None
            admin = self.User('admin', 'test1234')
            self._user_list.append(admin)
            self._is_initialized = True
            self.logger = logger.get_logger(__name__)

    class User():
        def __init__(self, username, password):
            self.username = username
            self.password = password

        def __repr__(self):
            return f"User(username={self.username}, password={self.password})"

    def add(self, a, b):
        result = a + b
        self.logger.info(f"the sum of {a} and {b} results in {result}", extra=self.log_properties)

        return result

    def subtract(self, a, b):
        result = a - b
        self.logger.info(f"Subtracting {b} from {a} results in {result}", extra=self.log_properties)
        return result

    def multiply(self, a, b):
        result = a * b
        self.logger.info(f"Multiplying {a} with {b} results in {result}", extra=self.log_properties)
        return result

    def divide(self, a, b):
        if b == 0:
            self.logger.error("Division by zero attempted", extra=self.log_properties)
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self.logger.info(f"Dividing {a} by {b} results in {result}", extra=self.log_properties)
        return result

    def register_user(self, username, password):
        for user in self._user_list:
            if user.username == username:
                self.logger.warning(f"User registration failed: {username} already exists", extra=self.log_properties)
                return None
        user = self.User(username, password)
        self._user_list.append(user)
        self.logger.info(f"Registered new user: {username}", extra=self.log_properties)
        return username

    def login(self, username, password):
        for user in self._user_list:
            if user.username == username and user.password == password:
                self._current_user = user
                self.logger.info(f"User {username} logged in", extra=self.log_properties)
                return username
        self.logger.warning(f"Login failed for user: {username}", extra=self.log_properties)
        return None

    def logout(self):
        user = self._current_user
        self._current_user = None
        if user:
             self.logger.info(f"User {user.username} logged out", extra=self.log_properties)
        else:
             self.logger.info("No user was logged in", extra=self.log_properties)
        return user

    def get_current_user(self):
        return self._current_user