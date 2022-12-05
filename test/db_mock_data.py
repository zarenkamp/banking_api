mock_customers = [
    "insert into customer (first_name, last_name) values ('Aguste', 'Suerz')",
    """insert into customer (first_name, last_name) values ('Junie', 'Spensly')""",
    """insert into customer (first_name, last_name) values ('Ali', 'Bolzmann')""",
    """insert into customer (first_name, last_name) values ('Robinet', 'Skatcher')""",
    """insert into customer (first_name, last_name) values ('Herbert', 'Vedstra')""",
    """insert into customer (first_name, last_name) values ('Rodrick', 'Tourry')""",
    """insert into customer (first_name, last_name) values ('Lynnet', 'Capaldi')""",
    """insert into customer (first_name, last_name) values ('Conchita', 'Calvard')""",
    """insert into customer (first_name, last_name) values ('Nicola', 'Beushaw')""",
    """insert into customer (first_name, last_name) values ('Franchot', 'Dumbrell')""",
]

mock_accounts = [
    """insert into account (owner, balance) values (6, 3950.82);""",
    """insert into account (owner, balance) values (1, 7419.3);""",
    """insert into account (owner, balance) values (9, 9308.24);""",
    """insert into account (owner, balance) values (9, 7598.6);""",
    """insert into account (owner, balance) values (7, 8097.46);""",
    """insert into account (owner, balance) values (6, 4486.23);""",
    """insert into account (owner, balance) values (9, 1469.32);""",
    """insert into account (owner, balance) values (6, 9765.52);""",
    """insert into account (owner, balance) values (2, 6941.7);""",
    """insert into account (owner, balance) values (5, 7882.19);""",
    """insert into account (owner, balance) values (9, 2341.83);""",
    """insert into account (owner, balance) values (10, 3711.12);""",
    """insert into account (owner, balance) values (10, 8936.01);""",
    """insert into account (owner, balance) values (1, 1934.68);""",
    """insert into account (owner, balance) values (3, 3582.78);""",
    """insert into account (owner, balance) values (3, 5418.51);""",
    """insert into account (owner, balance) values (6, 3650.64);""",
    """insert into account (owner, balance) values (1, 933.67);""",
    """insert into account (owner, balance) values (8, 3479.74);""",
    """insert into account (owner, balance) values (4, 2344.01);"""

]

mock_transfers = [
    f"""insert into transfer 
    (sending_customer, sending_account, receiving_customer, receiving_account, amount, transfer_date) 
    values (1, 2, 2, 9, 1000, datetime('now'))""",
    f"""insert into transfer 
    (sending_customer, sending_account, receiving_customer, receiving_account, amount, transfer_date) 
    values (2, 9, 1, 2, 1000, datetime('1997-07-16T19:20:30+01:00'))""",
    f"""insert into transfer 
    (sending_customer, sending_account, receiving_customer, receiving_account, amount, transfer_date) 
    values (2, 9, 1, 2, 5, datetime('2021-05-14T09:20:30+01:00'))""",
    f"""insert into transfer 
    (sending_customer, sending_account, receiving_customer, receiving_account, amount, transfer_date) 
    values (3, 15, 3, 16, 234, datetime('2022-12-14T07:21:30+01:00'))""",
    f"""insert into transfer 
    (sending_customer, sending_account, receiving_customer, receiving_account, amount, transfer_date) 
    values (7, 5, 3, 16, 25, datetime('2022-01-10T17:01:30+01:00'))""",

]