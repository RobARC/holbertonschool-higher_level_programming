# 0x0F. Python - Object-relational mapping

# Before you start…
Please make sure your MySQL server is in 5.7 -> [How to install MySQL 5.7 in Ubuntu 14.04](https://intranet.hbtn.io/rltoken/mqTU28SAIfz_-9w7rZipMw)
# Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

# Resources
<b>Read or watch:</b>

[Object-relational mappers](https://intranet.hbtn.io/rltoken/IqdjUaZ31ZfP6eT-lTyUkA)
[mysqlclient/MySQLdb documentation](https://intranet.hbtn.io/rltoken/rMJpVJ1_YjMWfvY00I7Kpw) /*(please don’t pay attention to _mysql)*/
[MySQLdb tutorials](https://intranet.hbtn.io/rltoken/DJz5W6Y13-6qUSTPTGrHYw)
[SQLAlchemy tutorials](https://intranet.hbtn.io/rltoken/9JWveMwNKe3IUErdEbDsUQ) 
[SQLAlchemys](https://intranet.hbtn.io/rltoken/E9dLS6Shaezq4ivnGxN_RA)
[mysqlclient/MySQLdbs](https://intranet.hbtn.io/rltoken/QFgtVxz2w-C1y1OB8uls1g) 
[Introduction to SQLAlchemys](https://intranet.hbtn.io/rltoken/I5bvhPGTOu3_-T-4jpN-hg) 
[Flask SQLAlchemys](https://intranet.hbtn.io/rltoken/UvaHESHeqlRA0Z0uQFi0_A) 
[10 common stumbling blocks for SQLAlchemy newbiess](https://intranet.hbtn.io/rltoken/Zb8Yc2WycLLYX8gnLlwZKw)
[Python SQLAlchemy Cheatsheets](https://intranet.hbtn.io/rltoken/XHPAX7-ydSou2BLWHII8Vw)
[SQLAlchemy ORM Tutorial for Python Developers](https://intranet.hbtn.io/rltoken/aeLSQ039BhLhamU2BjqsOw) (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)
[SQLAlchemy Tutorials](https://intranet.hbtn.io/rltoken/cmfi9C_nRXrmnwaJfCPyxA)

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
<li> Why Python programming is awesome</li>
<li> How to connect to a MySQL database from a Python script</li>
<li> How to SELECT rows in a MySQL table from a Python script</li>
<li> How to INSERT rows in a MySQL table from a Python script</li>
<li> What ORM means</li>
<li> How to map a Python Class to a MySQL table </li>

