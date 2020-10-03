<!-- @format -->

# SenecaLearning API

![version badge](https://img.shields.io/pypi/v/senecalearning) ![downloads badge](https://img.shields.io/pypi/pyversions/senecalearning) ![codefactor bage](https://img.shields.io/codefactor/grade/github/wyatt/seneca) ![commit badge](https://img.shields.io/github/last-commit/wyatt/seneca)

A small, unofficial python API for SenecaLearning. This in a _beta stage_ so please be prepared for bugs and issues. If anyone from SenecaLearning is reading this, a way to drastically improve this project is to introduce a way to create API keys. I am a student so updates may be erractic, but I hope to keep it as up to date as I can. If you can help improve this project in any way - create a pull request! I'm sure there's things I should be doing better and/or differently.

## Installation

`pip install senecalearning`

[PyPI link](https://pypi.org/project/senecalearning/)

## Usage

```python
import senecalearning
seneca = senecalearning.Login("<Your Login Token")
seneca.<method>
```

## How to get your login token

Unfortunately, Seneca doesn't provide an easy way to get a login token yet, so the only programmatic way I could find to do it was to use [Puppeteer](https://github.com/puppeteer/puppeteer) and scrape the response data. An [example](../examples/loginToken/) is in the examples folder. Please note, it uses NodeJS, not Python. Apparently there is a Python port of Puppeteer but I couldn't get it to work - perhaps someone smarter might be able to.

## Methods

### senecalearning.login()

```python
seneca = senecalearning.Login("<Your Login Token>")
```

Returns `None`. Required for authentication - SenecaLearning cannot be queried without it.

### senecalearning.getCoursesInfo(search="")

```python
seneca.getCoursesInfo(search="<search query>") #i.e. AQA Biology
# Can also be ran with no parameter
seneca.getCoursesInfo()
```

```python
#Example dictionary item
"Chemistry: AQA GCSE Higher" = {
  authors: ["Ewan Melling Flavell", "George Pidgeon", "Dr Eric Demoncheaux"]
  courseId: "e39e7f70-d100-11e7-9b85-bbf8589a9044"
  darkText: true
  description: "chem↵chemis"
  firstPublished: "2019-07-05T15:21:36.235Z"
  headerImageURL: "seneca-image-cdn:///2018-04/870d464e-1afb-40ed-a6e9-e675579a3f66/chemistry.jpg"
  id: "e39e7f70-d100-11e7-9b85-bbf8589a9044"
  regions: ["GB"]
  sectionIds: ["eb552340-d100-11e7-9b85-bbf8589a9044", "2a3d1970-d122-11e7-bce0-9d60619a6a6b",…]
  subscriptionTier: "FREE"
  tags: {29304df7-aad4-4b2f-ac43-2fb169c04ebd: [{id: "8b215c64-328d-4600-82b8-18cbe38ca289", value: "AQA"}],…}
  visibility: "PUBLIC"
}
```

Returns `nested dictionary`. It returns a dictionary with courses that contain the search term. The key is the course title and the value is the metadata associated with that course. Please note, if you run this with no search query, it will return all courses and their metadata - a large amount of data!

### senecalearning.getCourseInfo(courseId="")

```python
seneca.getCourseInfo(courseId="<course id>")
```

Returns `dict`. It returns a dictionary with metadata about the relevant course. The key is the course title.

### senecalearning.getCourseStats(courseId="")

```python
seneca.getCourseStats(courseId="<course id>")
```

Returns `nested dict`. It returns a dictionary with all the lessons you have studied in the specified course and their metadata

```python
#Example dictionary item
"Exam-Style Questions - Organic Compounds" = {
  averageScore: 0.9259259259259259
  averageSessionScore: 0.9259259259259259
  bestScore: 1
  courseId: "e39e7f70-d100-11e7-9b85-bbf8589a9044"
  lastScore: 1
  lastStudied: 1601323272
  moduleIdsIncorrectLast: []
  moduleIdsStudied: ["6ec3e9b0-819a-4d67-9a21-3669d382e6e4", "be975cda-eea5-48ad-97f3-d57bf7fa3910",…]
  proficiency: 1
  recentSectionEvents: [,…]
  sectionId: "131de50f-5cfc-4b68-8a27-9251409aaac2"
  sessionModulesCorrect: 25
  sessionModulesStudied: 69
  sessionsCompleted: 3
  studied: True
  spacing: 1.9807043651
  totalStudyTime: 466
  userId: "<REDACTED>"
  worstScore: 0.7777777777777778
}
```
