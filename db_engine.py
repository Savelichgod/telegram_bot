from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData, inspect, insert, select, delete, \
    Boolean, func, update


engine = create_engine('sqlite:///hardware_store.db')

metadata = MetaData()

products = Table('products', metadata,
                 Column('id', Integer, primary_key=True, autoincrement=True),
                 Column('name', String),
                 Column('user_id', Integer),
                 Column('is_ordered', Boolean, nullable=True),
                 )


def create_table():
    if not inspect(engine).has_table("products"):
        products.create(engine)


def append_to_table(name, user_id):
    with engine.connect() as conn:
        conn.execute(insert(products), [{
            'name': name,
            'user_id': user_id
        }])
        conn.commit()


def get_products(user_id):
    with engine.connect() as conn:
        return conn.execute(select(products.c.name).where(products.c.user_id == user_id))


def get_max_product_id():
    with engine.connect() as conn:
        return conn.execute(select(func.max(products.c.id))).first()[0]


def delete_line(index):
    with engine.connect() as conn:
        conn.execute(delete(products).where(products.c.id == index))
        conn.commit()


def clear_database():
    with engine.connect() as conn:
        conn.execute(delete(products))
        conn.commit()


def get_first_id():
    with engine.connect() as conn:
        return conn.execute(select(func.min(products.c.id))).first()[0]


def get_all_id():
    with engine.connect() as conn:
        return conn.execute(select(products.c.id)).fetchall()


def set_ordered(is_ordered, product_id):
    with engine.connect() as conn:
        conn.execute(update(products).
                     where(products.c.id == product_id).
                     values(is_ordered=is_ordered)
                     )
        conn.commit()


def get_ordered_names():
    with engine.connect() as conn:
        return conn.execute(select(products.c.name).
                            where(products.c.is_ordered == True)).fetchall()


def get_ordered_ids():
    with engine.connect() as conn:
        return conn.execute(select(products.c.id).
                            where(products.c.is_ordered == True)).fetchall()