import numpy as np
import pandas as pd
from faker import Faker
fake = Faker()

users = [(fake.name(), fake.address(), fake.email(), np.random.randint(20, 60), np.random.normal(loc=50000, scale=15000)) for _ in range(100)]

df = pd.DataFrame(users, columns=['name', 'address', 'email', 'age', 'income'])
print(df.head(10))
