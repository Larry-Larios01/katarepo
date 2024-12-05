<script lang="ts">
import { ref, defineComponent } from 'vue';

export default defineComponent({
  name: 'Cronometer',

  props: {
    laps: {
      type: Number, 
      default: 10,   
    },
    names: {
      type: String,  
      default:  "unknow",
    },
  },


  setup(props) { 
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

    
    const evaluate = () => numbers.value.length < props.laps;

    
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
    <button v-on:click="start"> start </button>
    <button v-on:click="pause">pause</button>
    <button v-on:click="stop"> stop </button>
    <button v-show="evaluate()" @click="lap">lap</button>
    <p>{{ count }}</p>

    <li v-for="lap in numbers">
        {{ lap }}
    </li>   

</template>