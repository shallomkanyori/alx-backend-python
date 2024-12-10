"""This module runs multiple database queries concurrently"""
import aiosqlite
import asyncio

async def async_fetch_users():
    """Fetches all users from the database"""
    async with aiosqlite.connect('users.db') as conn:
        cursor = await conn.execute("SELECT * FROM users")
        return await cursor.fetchall()

async def async_fetch_older_users():
    """Fetch users older than 40"""

    async with aiosqlite.connect('users.db') as conn:
        cursor = await conn.execute("SELECT * FROM users WHERE age > 40")
        return await cursor.fetchall()
    

async def fetch_concurrently():
    """Fetch users concurrently"""
    users, older_users = await asyncio.gather(async_fetch_users(), async_fetch_older_users())
    return users, older_users

users, older_users = asyncio.run(fetch_concurrently())
print(f"All users: {users}")
print(f"Users over 40: {older_users}")