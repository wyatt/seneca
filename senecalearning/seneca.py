import requests
import json

class login:
  def __init__(self, token=None):
    self.token = token
    self.senecaHeaders = {
        "access-key": self.token,
        "content-type": "application/json",
        "correlationid": ""
    }
    if not token:
      self.notoken()
  def notoken(self):
    print("Error. Please provide a token")
    return False
  def getCoursesInfo(self, search=None):
    self.search = search
    try:
      body = json.dumps({"size": 2000})
      self.senecaHeaders["correlationid"] = "1601311776393::380f3b280adc675d0f19168aaece5377"
      response = json.loads(requests.post(
          "https://course.app.senecalearning.com/api/courses/queryCourses", headers=self.senecaHeaders, data=body).text)["results"]["hits"]
    except requests.exceptions.RequestException as e:
      raise SystemExit(e)
    if self.search:
      matches = {}
      for course in response:
        if self.search in course["_source"]["name"]:
          name = course["_source"]["name"].rstrip()
          matches[name] = {}
          del course["_source"]["name"]
          matches[name] = course["_source"]
        else:
          continue
      return matches
    allCourses = {}
    for course in response:
        name = course["_source"]["name"].rstrip()
        allCourses[name] = {}
        del course["_source"]["name"]
        allCourses[name] = course["_source"]
    return allCourses

  def getCourseInfo(self, courseId=None):
    self.courseId = courseId
    try:
      self.senecaHeaders["correlationid"] = "1601321310216::fd9a102ee3fae8831161503a13668f7c"
      response = json.loads(requests.get(
          f"https://course-cdn-v2.app.senecalearning.com/api/courses/{self.courseId}/sections", headers=self.senecaHeaders).text)["course"]
    except requests.exceptions.RequestException as e:
      raise SystemExit(e)
    return response
  
  def getCourseStats(self, courseId=None):
    self.courseId = courseId
    if courseId:
      stats = {}
      try:
        self.senecaHeaders["correlationid"] = "1601321310197::866588fb985024c4395d76098d47cd09"
        response = json.loads(requests.get(
            f"https://stats.app.senecalearning.com/api/stats/sections?courseId={self.courseId}", headers=self.senecaHeaders).text)["stats"]
      except requests.exceptions.RequestException as e:
        raise SystemExit(e)
      for item in response:
        stats[item["sectionId"]] = item
      try:
        self.senecaHeaders["correlationid"] = "1601321310216::fd9a102ee3fae8831161503a13668f7c"
        response = json.loads(requests.get(f"https://course-cdn-v2.app.senecalearning.com/api/courses/{self.courseId}/sections", headers=self.senecaHeaders).text)["sections"]
      except requests.exceptions.RequestException as e:
        raise SystemExit(e)
      for item in response:
        if item["id"] in stats:
          if item["moduleIds"]:
            stats[item["title"]] = stats.pop(item["id"])
            stats[item["title"]]["studied"] = True
        else:
          title = item["title"]
          del item["title"]
          stats[title] = item
          stats[title]["studied"] = False
      return stats
    print("Please provide a course ID")
    return