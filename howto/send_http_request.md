### js(xhr)
> example from: http://vanilla-js.com/

```js
// native js:
var r = new XMLHttpRequest();
r.open("POST", "path/to/api", true);
r.onreadystatechange = function () {
  if (r.readyState != 4 || r.status != 200) return;
  alert("Success: " + r.responseText);
};
r.send("banana=yellow");

// example with jquery:
$.ajax({
  type: 'POST',
  url: "path/to/api",
  data: "banana=yellow",
  success: function (data) {
    alert("Success: " + data);
  },
});
```

### python

```py
# with: requests
import requests as R
try:
    response = R.post('URL',{'banana':'yellow'})
except:
    pass
else:
    print (response.content)
```

