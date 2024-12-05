<script lang="ts">
import { ref, defineComponent } from 'vue';

export default defineComponent({
  name: 'cronometer',

 
  setup() { // Props es recibido aquí
    const count = ref(0);
    let cronometer: number;
    const numbers = ref<number[]>([]);

    function start() {
      cronometer = setInterval(() => {
        count.value++;
      }, 1000);
    }

    function pause() {
      clearInterval(cronometer);
    }

    function stop() {
      count.value = 0;
      clearInterval(cronometer);
      numbers.value = [];
    }

    function lap() {
      numbers.value.push(count.value);
    }

    // Ahora puedes usar props.laps
    const evaluate = () => numbers.value.length < props.laps;

    // Exponer las funciones y propiedades al template
    return {
      start,
      count,
      stop,
      pause,
      lap,
      numbers,
      evaluate,
    };
  },
});
</script>

<template>
    <button @click="start"> start </button>
    <button @click="pause">pause</button>
    <button @click="stop"> stop </button>
    <button v-if="evaluate()" @click="lap">lap</button>
    <p>{{ count }}</p>

    <li v-for="lap in numbers">
        {{ lap }}
    </li>   

</template>