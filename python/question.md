## 정규표현식

### Q. 핸드폰 번호를 매칭하는 패턴을 만들어봐라.

```python
import re

def validate_phone_number(number):
    #==================================#
    pattern = ""
    #==================================#
    if not re.match(pattern, number):
        return "휴대폰 번호가 아닙니다."
    else:
        return "휴대폰 번호입니다."
```
