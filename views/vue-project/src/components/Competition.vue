<script lang="ts">
import { isTemplateExpression } from 'typescript';
import { ref , defineComponent} from 'vue'

export default defineComponent({

    name: 'Competition',

    props: {
    players: {
      type: Number
    },
    laps: {
        type: Number,
        default: 1000,
    },

  },
  
  setup() {


    
   



    // don't forget to expose the function as well.
    return {
 
    }
  }
})



