//What's the result of OR?
alert(null || 2 || undefined); // it will print 2
//What's the result of OR'ed alerts
alert(alert(1) || 2 || alert(3)); // it will first print 1, then 2
//What is the result of AND?
alert(1 && null && 2); // null
//What's the result of AND'ed alerts
alert(alert(1) && alert(2)); // it will print 1
//The result of OR AND OR
alert(null || (2 && 3) || 4); // it will print 3
