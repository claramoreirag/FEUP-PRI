# Makefile

#Rules

all: fake_clean.csv article.csv thread.csv type.csv website.csv author.csv fake.db

# Clean the dataset
fake_clean.csv: fake.csv
	python data_cleaning.py
	python data_analysis.py
	echo "Data cleaning and analysis done!"


# Split the clean dataset into "tables" to make the database
article.csv thread.csv type.csv website.csv author.csv: fake_clean.csv
	python split.py
	echo "Spliting finished, the new posts are ready"

# Create an SQL database with the information of the csv's resulting from the spliting 
fake.db: article.csv thread.csv type.csv website.csv author.csv
	python to_sqlite.py
	echo "Database created, fake.db ready"

clean:
	rm -f fake_clean.csv article.csv thread.csv type.csv website.csv author.csv