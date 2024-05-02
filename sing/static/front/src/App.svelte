<script>
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
  import './app.css'

  let rand=-1;
  function getRand(){
    fetch("http://127.0.0.1:5000/rand")
    .then(d=>d.text())
    .then(d=>(rand=d));
  }
</script>

<main>
  <h1>Your number is {rand}!</h1>
  <button on:click={getRand}>Get a random number</button>
  <div>
    <a href="https://vitejs.dev" target="_blank" rel="noreferrer">
      <img src={viteLogo} class="logo" alt="Vite Logo" />
    </a>
    <a href="https://svelte.dev" target="_blank" rel="noreferrer">
      <img src={svelteLogo} class="logo svelte" alt="Svelte Logo" />
    </a>
  </div>
  <h1 class="text-green-200">Vite + Svelte</h1>

  <div class="bg-red-400">
    <Counter />
  </div>

  <p>
    Check out <a href="https://github.com/sveltejs/kit#readme" target="_blank" rel="noreferrer">SvelteKit</a>, the official Svelte app framework powered by Vite!
  </p>

  <p class="font-extrabold">
    Click on the Vite and Svelte logos to learn more
  </p>
</main>

<!-- <style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
</style> -->
