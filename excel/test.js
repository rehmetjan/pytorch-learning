function calculateDaysBetweenDates(begin, end) {
  var beginDate = new Date(begin)
  var endDate = new Date(end)
  var days = (endDate - beginDate) / (1000 * 60 * 60 * 24)
  return days
}

var a = calculateDaysBetweenDates('2017-12-13', '2017-12-22')
console.log(a)
