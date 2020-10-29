CREATE TABLE titles (
	titleID VARCHAR(255) NOT NULL,
	ordering INT NOT NULL,
	title VARCHAR(255) NOT NULL,
	region VARCHAR(255),
	language VARCHAR(255),
	attributes TEXT(65535),
	isOriginalTitle BOOLEAN,
	PRIMARY KEY (titleID)
	);

CREATE TABLE titleTypes (
	titleID VARCHAR(255) NOT NULL,
	alternative BOOLEAN,
	dvd BOOLEAN,
	festival BOOLEAN,
	tv BOOLEAN,
	video BOOLEAN,
	working BOOLEAN,
	original BOOLEAN,
	imdbDisplay BOOLEAN,
	PRIMARY KEY (titleID)
	);

CREATE TABLE titleBasics (
	tconst VARCHAR(255) NOT NULL,
	titleType VARCHAR(255),
	primaryTitle VARCHAR(255),
	originalTitle VARCHAR(255) NOT NULL,
	isAdult BOOLEAN NOT NULL,
	startYear YEAR NOT NULL,
	endYear YEAR,
	runtimeMinutes INT NOT NULL,
	genres VARCHAR(255)
	PRIMARY KEY (tconst)
	);

CREATE TABLE principals (
	tconst VARCHAR(255) NOT NULL,
	ordering INT NOT NULL,
	nconst VARCHAR(255) NOT NULL,
	category VARCHAR(255),
	job VARCHAR(255),
	character VARCHAR(255),
	PRIMARY KEY (nconst),
	FOREIGN KEY (tconst)
		REFERENCES titles(titleID)
	);
	
CREATE TABLE ratings (
	tconst VARCHAR(255) NOT NULL,
	averageRating FLOAT(2) NOT NULL,
	numVotes INT,
	PRIMARY KEY (tconst)
	);
	
CREATE TABLE nameBasics (
	nconst VARCHAR(255) NOT NULL,
	primaryName VARCHAR(255) NOT NULL,
	birthYear YEAR NOT NULL,
	deathYear YEAR,
	primaryProfession VARCHAR(255),
	knownForTitles VARCHAR(255),
	PRIMARY KEY (nconst)
	);


	
