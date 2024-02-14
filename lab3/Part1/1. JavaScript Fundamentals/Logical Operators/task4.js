if (-1 || 0) alert("first"); // will print (true || false == true)
if (-1 && 0) alert("second"); // will not print (true && false == false)
if (null || (-1 && 1)) alert("third"); // will print (false || true && true == false || true == true)
