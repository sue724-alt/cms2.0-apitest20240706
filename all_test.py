import time

import pytest
import os
if __name__ == '__main__':
    pytest.main()
    time.sleep(1)
    os.system("allure generate ./temp -o ./reports --clean")

