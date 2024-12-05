<script lang="ts">
import { ref , defineComponent} from 'vue'

export default defineComponent({

    name: 'Competition',

    props: {
    players: {
      type: Number,
      default:5
    },
    laps: {
        type: Number,
        default: 1000,
    },

  },
  
  setup(props) {


    const inputs = ref(Array(props.players).fill(""));



   function submitValues()
   {
    alert(inputs.value)

   }


   

   



    // don't forget to expose the function as well.
    return {
      inputs,
      submitValues
 
    }
  }
});

</script>


<template>
  <div>
    <div v-for="(item, index) in inputs" :key="index">
      <input
        type="text"
        v-model="inputs[index]"
        placeholder="Enter value"
      />
    </div>
    <button v-on:click="submitValues()">Submit</button>
  </div>
</template>





