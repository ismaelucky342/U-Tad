# Research project entities and relationships DB

The research topic will focus on the importance of the correct identification of entities and their relationships when developing a relational database model, exposing the possible consequences in the physical implementation of an incorrect model.

### Points on which to argue the exhibitions:

- Possible implications in relationships identified as entities.

- Possible loss of information from an erroneous approach

- Possible implications on table storage and management when dealing with duplicate information.

# Project

The correct identification of relationships and their corresponding entities is essential so that we can ensure the functioning and efficiency of the data that is stored. This involves understanding the entities in an app's domain, as well as the relationships between them.

### Implications on Relationships Identified as Entities:

Query performance is directly affected by the correct choice of a so-called "parent entity" and the efficiency of establishing relationships. A bad design can lead to complicated and slow queries, harming the system's response. Additionally, data consistency may be at risk if relationships are not properly defined, which could result in contradictory and confusing information.

### Loss of Information in Erroneous Approaches:

Incorrect identification of relationships can lead to inappropriate normalization, fragmenting the data in unwanted ways. This not only makes the overall understanding of the model difficult, but can also negatively affect the adaptability of the system to future changes. The lack of referential integrity, a result of poorly defined primary and foreign keys, directly impacts the reliability of stored data and makes critical actions difficult.

### Implications on Table Storage and Management:

Data redundancy, caused by improper identification of entities and relationships, can lead to inefficient use of storage space and increase operating costs. Additionally, managing duplicate data becomes more complex, affecting the consistency and reliability of information. In terms of maintainability, a poor design can make it difficult to expand and modify the system, consuming more time and resources.





![image](https://github.com/ismaelucky342/U-Tad/assets/153450550/62bc16fd-1d63-401e-962d-b090cad59bdc)
