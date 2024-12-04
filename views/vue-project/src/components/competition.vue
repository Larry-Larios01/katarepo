<script lang="ts">
import { ref , defineComponent, mergeProps} from 'vue'

export default defineComponent({

    name: 'competition',

    props: {
    players: {
      type: Number,
    },
    laps: {
        type: Number,
        default: 1000,
    },

  },
  
  setup() {
    
    const count = ref(0)
    let cronometer : number;
    const numbers = ref<number[]>([]);
    function start() {
    cronometer = setInterval(() => {
    count.value++;
        }, 1000)
    }

    function pause() {
    clearInterval(cronometer)
    }

    function stop() {
    count.value = 0
    clearInterval(cronometer)
    numbers.value = []
    }

    function lap() {
        numbers.value.push(count.value)
    
    }

    const evaluate = () => numbers.value.length < props.laps; 



    // don't forget to expose the function as well.
    return {
      start,
      count,
      stop,
      pause, 
      lap,
      numbers,
      evaluate
    }
  }
})