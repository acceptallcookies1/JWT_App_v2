document.getElementById("fetchData").addEventListener("click", async () => {
    const response = await fetch('https://your-backend-api-url.com/data');
    const data = await response.json();
    console.log(data);
    alert(`Data fetched: ${JSON.stringify(data)}`);
  });
  