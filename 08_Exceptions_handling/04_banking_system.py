class InvalidAmountError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


class DailyLimitExceededError(Exception):
    pass


class BankAccount:
    def __init__(self, owner, balance, daily_limit, max_withdrawals):
        self.owner = owner
        self.balance = balance
        self.daily_limit = daily_limit
        self.max_withdrawals = max_withdrawals

        self.daily_taken = 0
        self.daily_withdrawals = 0

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(f"Amount must be positive, got {amount}")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(f"Amount must be positive, got {amount}")

        if amount > self.balance:
            raise InsufficientFundsError(
                f"Attempted to withdraw {amount}, but balance is {self.balance}"
            )

        if self.daily_taken + amount > self.daily_limit:
            raise DailyLimitExceededError(
                f"Daily limit exceeded: trying to withdraw {self.daily_taken + amount}, limit is {self.daily_limit}"
            )

        if self.daily_withdrawals >= self.max_withdrawals:
            raise DailyLimitExceededError(
                f"Maximum withdrawals per day reached: {self.max_withdrawals}"
            )

        self.balance -= amount
        self.daily_taken += amount
        self.daily_withdrawals += 1

    def transfer_to(self, other_account, amount):
        # ако withdraw хвърли грешка, тя се "прехвърля" нагоре автоматично
        self.withdraw(amount)
        other_account.deposit(amount)

    def reset_daily_limits(self):
        self.daily_taken = 0
        self.daily_withdrawals = 0

    def __repr__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"


# приемаме, че класът BankAccount и грешките вече са дефинирани от теб по-горе

acc1 = BankAccount("Alice", 100, daily_limit=200, max_withdrawals=2)
acc2 = BankAccount("Bob", 50, daily_limit=200, max_withdrawals=2)

# 1) Невалидни суми
try:
    acc1.deposit(0)
except InvalidAmountError as e:
    print("Invalid deposit:", e)

try:
    acc1.withdraw(-10)
except InvalidAmountError as e:
    print("Invalid withdraw:", e)

# 2) Недостатъчна наличност
try:
    acc1.withdraw(999)
except InsufficientFundsError as e:
    print("Insufficient funds:", e)

# 3) Дневен лимит по сума
acc1.reset_daily_limits()
acc1.balance = 500
try:
    acc1.withdraw(300)   # daily_limit = 200
except DailyLimitExceededError as e:
    print("Daily limit (amount):", e)

# 4) Дневен лимит по брой тегления
acc1.reset_daily_limits()
try:
    acc1.withdraw(50)
    acc1.withdraw(50)
    acc1.withdraw(50)    # max_withdrawals = 2
except DailyLimitExceededError as e:
    print("Daily limit (count):", e)

# 5) Успешен трансфер
acc1 = BankAccount("Alice", 200, 500, 5)
acc2 = BankAccount("Bob", 50, 500, 5)
acc1.transfer_to(acc2, 100)
print(acc1, acc2)

# 6) Неуспешен трансфер (недостатъчна наличност)
try:
    acc1.transfer_to(acc2, 999)
except Exception as e:
    print("Failed transfer:", e)