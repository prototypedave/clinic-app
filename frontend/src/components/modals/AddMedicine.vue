<template>
    <div v-if="alert.visible" class="fixed top-4 right-4 bg-green-500 text-white p-4 rounded-md shadow-lg z-50">
        {{ alert.message }}
    </div>
    <button class="flex flex-col p-4 bg-violet-800 justify-between items-center text-white hover:bg-violet-950 rounded-md" @click="openModal = true">
        <BeakerIcon class="justify-center size-8" aria-hidden="true" />
        <p>Medicine/Lab</p>
    </button>

    <div v-if="openModal" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-4xl shadow text-violet-950">   
        <h2 class="text-xl font-bold mb-4 text-center">Medicine Data Form</h2>
        <form @submit.prevent="submitMedicine">
          <div class="grid grid-cols-3 gap-4">
            <div>
              <label for="medicineName" class="block text-sm text-left mb-2 font-medium">Medicine Name</label>
              <input v-model="medicineName" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" placeholder='Name' required />
            </div>
            <div>
              <label for="manufacturer" class="block text-sm text-left mb-2 font-medium ">Manufacturer</label>
              <input v-model="manufacturer" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder='Company Name' required />
            </div>
            <div>
                <label for="classificaton" class="block text-sm text-left mb-2 font-medium">Medicine Type</label>
                <multiselect v-model="classification" tag-placeholder="" placeholder="Search or add classification" label="name" track-by="name" :options="options" :multiple="true" :taggable="true" @tag="addTag" class="text-xs"></multiselect>
            </div>
            <div>
              <label for="quantity" class="block text-sm text-left mb-2 font-medium ">Quantity</label>
              <input v-model="quantity" type="number" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder='0' required />
            </div>
             <div>
              <label for="dosage" class="block text-sm text-left mb-2 font-medium ">Dosage</label>
              <select v-model="dosage" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder='Tablet' required>
                <option value="liquid">Liquid</option>
                <option value="tablet">Tablet</option>
                <option value="cream">Cream</option>
              </select>
            </div>
             <div>
              <label for="strength" class="block text-sm text-left mb-2 font-medium ">Strength</label>
              <input v-model="strength" type="number" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder='10mg' required />
            </div>
            <div>
              <label for="unit" class="block text-sm text-left mb-2 font-medium ">Unit</label>
                <select v-model="unit" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder='mg' required>
                    <option value="g">g</option>
                    <option value="mg">mg</option>
                    <option value="ml">mL</option>
                </select>
            </div>
              <div>
              <label for="purchaseDate" class="block text-sm text-left mb-2 font-medium ">Purchase Date</label>
              <input 
                  v-model="purchaseDate" 
                  type="date" 
                  class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm" 
                  :max="today"
                  @input="validateDate" 
                  required 
              />
              <p v-if="dateError" class="text-red-500 text-sm mt-2">{{ dateError }}</p>
            </div>
            <div>
              <label for="expiryDate" class="block text-sm text-left mb-2 font-medium ">Expiry Date</label>
              <input 
                  v-model="expiryDate" 
                  type="date" 
                  class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm" 
                  :min="today" 
                  @input="validateDate" 
                  required 
              />
              <p v-if="expiryError" class="text-red-500 text-sm mt-2">{{ expiryError }}</p>  
            </div>
            <div>
              <label for="price" class="block text-sm text-left mb-2 font-medium ">Purchase Price</label>
              <input v-model="price" type="number" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder="$" required />
            </div>
            <div>
              <label for="supplier" class="block text-sm text-left mb-2 font-medium ">Supplier</label>
              <input v-model="supplier" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder="Supplier Company Name" required />
            </div>
            <div>
              <label for="category" class="block text-sm text-left mb-2 font-medium ">Category</label>
              <input v-model="category" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder="Antibiotics" required />
            </div>         
          </div>
          <div class="flex justify-end gap-2">
              <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">submit</button>  
              <button @click="openModal = false" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">close</button>
          </div>
        </form>
      </div>
    </div>
</template>

<script>
    import { BeakerIcon } from '@heroicons/vue/20/solid';
    import Multiselect from 'vue-multiselect';

    export default {
        components: { Multiselect, BeakerIcon },
        data () {
          return {
            classification: null,
            options: [
                { name: 'Analgesics' }, 
                { name: 'Antibiotics' }, 
                { name: 'Antivirals' },
                { name: 'Antifungals' },
                { name: 'Antacids' },
                { name: 'Antihistamines' },
                { name: 'Cardiovascular' },
                { name: 'Endocrine' },
                { name: 'Psychotropics' },
                { name: 'Vaccines' },
                { name: 'Anti-inflammatory' },
                { name: 'Dermatological' },
                { name: 'Gastrointestinal' },
                { name: 'Respiratory' },
                { name: 'other' },

            ],
            openModal: false,
            alert: {visible: false, message: ''},
            today: new Date().toISOString().split('T')[0],
            dateError: '',
            expiryError: ''
          }
        },
        methods: {
            addTag (newTag) {
              const tag = {
              name : newTag }
              this.options.push(tag)
            }
        }
    }

    
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>