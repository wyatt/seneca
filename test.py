import seneca

senecalogin = seneca.login("<API Token here>")
stats = senecalogin.getCourseStats(id="e39e7f70-d100-11e7-9b85-bbf8589a9044")
for key, item in stats.items():
  print(f"{key} - {item['studied']}")