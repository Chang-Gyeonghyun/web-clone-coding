# Greeting.js

`document.querySelector()`�� ���ؼ� �ش� html�±�, id, class�� ������ �� �ִ�. �� �Լ��� �� ���� ���� �ҷ�����, ���� class�� ���� ���� �±׵��� �������� ���ؼ� All�� �ٿ� ����Ѵ�.

```jsx
const loginForm = document.querySelector("#login-form");
```

### ���� ����

- `const` �ʱ�ȭ�� �Ǿ�� �ϸ� ������ �Ұ����ϴ�. ��Է� �� Ÿ������ �����Ѵ�.
- `let` ������ ������ �����ϴ�.

### Class����

- `document.querySelector()` ���� ������ �޾Ƽ� ������ ������ �Ͽ���. `.classList` �� ���� ��ü�� ������ �ִ� Ŭ�������� ���� ���캼 �� �ְ�, Ŭ������ �ְ� ���� �۾��� �� �� �ִ�.

```css
.hidden{
    display: none;
}
```

���� ��� `.hidden` ��� Ŭ������ �ְ� ���� �۾��� �����ν� �������� ��ҵ��� ������ �� �ִ�.

- `��ü.innerText` �� ���� HTML������ �ؽ�Ʈ�� �ٲ� �� �ִ�.

### formating

`�����ڿ���` �� `�����ڿ���` �� �ƴ� ``${������}`` �� �̿��Ͽ� format�� �� �� �ִ�. 

### localstroage

���������� localstorage�� �����Ѵ�. ������ ���� ���� �����ͺ��̽��� ����. `form` �±׸� ���� �����ϰ� �ǰų�, ���� ���� ��ħ �� ��� ������ �� �����ʹ� �ʱ�ȭ�� �ȴ�. �̸� �����ϱ� ���ؼ� localstorage�� �����Ѵ�. `localstorage.setItem(key, value)` �� ������ �� �ִ�. �̿� ����� dictinary�� �ſ� �����ϴ�. 

### EventListner

���� �����⡯ �ϰų� �Ǵ� ��ư�� ��Ŭ���� �� ���� ���� �̺�Ʈ�� �߻��Ѵ�. `document.querySelector()` �� ��ü�� �޾� �����ϰ�, �ش� ��ü�� ���� `.addEventListener("�̺�Ʈ", �Լ�)` �� ���� �ش� �̺�Ʈ�� �߻����� �� �Լ��� �۵��� �� �ִ�. �Լ��� ���ڷ� ����� �� ()�� ���� �ʵ��� �Ѵ�.

- �۵� ��ų �Լ��� ������ ��, �Լ��� �Ķ���ͷ� event�� ���� �� �ִ�. `event.preventDefault()` �� ���� �ش� �̺�Ʈ�� �߻��ϴ� ���� ���� �Ӵ��� �ٸ� �޼ҵ带 Ȱ���Ͽ� �پ��� �ڵ带 �ϼ��� �� �ִ�.

---

# clocks.js

### Date()

- `const date = new Date();` �ڵ带 ���� ���� �ð��� �ҷ��� �� �ִ�. ��ü�� �żҵ带 Ȱ���Ͽ� �ð�, ��¥, �� �⵵�� �ҷ��� �� �ִ�.
- `setInterval(�Լ�, ��)` �ش� �Լ��� ������ �ʸ� �������� ����ǰ� �Ѵ�.
- `.padStart(����, "����")` �ش� string ��ü ���� ������ ���ڿ� �°� ���ڸ� ä�� �ִ´�.

---

# quotes.js

### Math

- `Math.floor` ���ڸ� �����Ѵ�.
- `Math.random()` 0���� 1������ ���ڸ� �����ϰ� ǥ���Ѵ�. ���ϴ� ������ �ִٸ�, �� ���ڸ�ŭ ���ϸ� �ȴ�.

---

# background.js

### HTML�±� �����

- `document.createElement("�±�")` ���� ���� �±׸� ���� �� �ִ�.
    - �±װ� �����Ǹ� �ش� �±װ� ������ �Ӽ� ���� js������ ���� �����Ѵ�.
- `.appendChild(�±� ����)` �±׸� ��ġ�� ���� �����Ѵ�. �ش� ��ü�� �ڽ� ��ҷ� ����.

---

# weather.js

### ��ġ�� ��Ÿ���� �Լ�

```jsx
navigator.geolocation.getCurrentPosition(onGeoOk,onGeoError);
```

js�� �⺻���� ����ִ� ����̴�. ù ��° ���ڴ� ���� ��ġ�� �̺�Ʈ�� �޴´�`. coords` �� ���� ������ �浵�� ���� �� �ִ�.

```jsx
fetch(url).then(response => response.json())
    .then((data) => {
        const weather = document.querySelector("#weather span:first-child");
        const city = document.querySelector("#weather span:last-child");
        city.innerText = data.name;
        weather.innerText = `${data.weather[0].main} / ${data.main.temp}`;
    })
```

- fetch�� url�� �ҷ��´�. �� �۾��� �ð��� ���� ��ƸԴµ� ��ǻ�ʹ� pipeline ���·� ���� �ٹ������� �۾��� �����Ѵ�. ���� �ش� �����͸� ��⵵ ���� ���� �ڵ带 �����ع��� �� �ִٴ� ���̴�.
- `.then` �� ��ü�� ����Ǿ�� ���� �ڵ尡 ����� �� �ְ� �����Ѵ�. `response` �� �����͸� �ҷ����� `json` ���� ��ȯ��Ų��. ���� ���� �����͵��� �����Ͽ� Ȱ���� �� �ִ�.

---

# toDo.js

�ռ� ����� ������� ���� Ȱ���Ѵ�. 

to do ����� ����� ����� �۾��� �Ѵ�. ������ ���� �� ����� ������ ������ �� ���� ����� ���ÿ� �������� ������ �� �׸� ���� ID�� ������ �Ѵ�. �� Date�� �̿��� �ð��� ���� �ٸ� �� ����

- to do ����Ʈ�� ������ ���� ����ǰ� �Ͽ��� log in �Ͽ��� �� ����� ǥ�õǵ��� �Ѵ�.
    - ����Ʈ ������ localstorage�� �����Ѵ�. ������ �� DB�� string�� �����ϱ� ������ Ÿ�� ��ȯ ������� �Ѵ�. �� `JSON.stringify(��ü)` �� Ÿ�� ��ȯ ��ų �� �ִ�.
    - filter�Լ� �� lamda���� Ȱ���Ͽ� ����Ʈ�� ������ �� �ִ�.
    
    ```jsx
    	 toDos = toDos.filter((toDo) => toDo.id !== parseInt(li.id));
    ```
    

---

## Website-preview

![homepage](pages_image/homepage.png)

![loginpage](pages_image/loginpage.png)


