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
        <form @submit.prevent="addMedicineData">
          <div class="grid grid-cols-3 gap-4">
            <div>
              <label for="name" class="font-medium text-sm text-left block nb-2">Medicine</label>
              <input id="name" v-model="name" type="text" class="text-sm block pl-2 py-2 mt-1 border rounded-md shadow-sm focus:border-violet-950 w-full" required  placeholder="Medicine Name"/>
            </div>
            <div>
              <label for="batch" class="font-medium text-sm text-left block nb-2">Batch No.</label>
              <input id="batch" v-model="batch" type="text" class="text-sm block pl-2 py-2 mt-1 border rounded-md shadow-sm focus:border-violet-950 w-full" required  placeholder="Batch number"/>
            </div>
            <div>
              <label for="expiry" class="font-medium text-sm text-left block nb-2">Expiry Date</label>
              <input id="expiry" v-model="expiry" type="date" class="text-sm block pl-2 py-2 mt-1 border rounded-md shadow-sm focus:border-violet-950 w-full" required />
            </div>            
            <div>
              <label for="qty" class="font-medium text-sm text-left block nb-2">Quantity</label>
              <input id="qty" v-model="qty" type="number" class="text-sm block pl-2 py-2 mt-1 border rounded-md shadow-sm focus:border-violet-950 w-full" required  placeholder="0"/>
            </div>
            <div>
              <label for="mfcg" class="font-medium text-sm text-left block nb-2">Manufacturer</label>
              <input id="mfcg" v-model="mfcg" type="text" class="text-sm block pl-2 py-2 mt-1 border rounded-md shadow-sm focus:border-violet-950 w-full" required  placeholder="Manufacturer"/>
            </div>
            <div>
              <label for="supplier" class="font-medium text-sm text-left block nb-2">Supplier</label>
              <input id="supplier" v-model="supplier" type="text" class="text-sm block pl-2 py-2 mt-1 border rounded-md shadow-sm focus:border-violet-950 w-full" required  placeholder="Supplier"/>
            </div>
            <div>
              <label for="type" class="font-medium text-sm text-left block nb-2">Medicine Type</label>
              <Multiselect mode="multiple" v-model="type" required max=4 :options="options"/>
            </div>
            <div>
              <label for="admin" class="font-medium text-sm text-left block nb-2">Mode of Intake</label>
              <Multiselect v-model="admin" required max=4 :options="selections"/>
            </div>
            <div>
              <label for="form" class="font-medium text-sm text-left block nb-2">Dosage Form</label>
              <Multiselect v-model="form" required max=4 :options="dosage"/>
            </div>
            <div>
              <label for="strength" class="font-medium text-sm text-left block nb-2">Strength</label>
              <input id="strength" v-model="strength" type="number" class="text-sm block pl-2 py-2 mt-1 border rounded-md shadow-sm focus:border-violet-950 w-full" required  placeholder="in mg"/>
            </div>
            <div>
              <label for="cost" class="font-medium text-sm text-left block nb-2">Unit Cost</label>
              <input id="cost" v-model="cost" type="number" class="text-sm block pl-2 py-2 mt-1 border rounded-md shadow-sm focus:border-violet-950 w-full" required  placeholder="0"/>
            </div>
            <div>
              <label for="price" class="font-medium text-sm text-left block nb-2">Unit Price</label>
              <input id="price" v-model="price" type="number" class="text-sm block pl-2 py-2 mt-1 border rounded-md shadow-sm focus:border-violet-950 w-full" required  placeholder="0"/>
            </div>
          </div>
          <div class="flex justify-center gap-2 mt-4">
            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">submit</button>  
            <button @click="openModal = false" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">close</button>
          </div>
          
        </form>
      </div>
    </div>
</template>

<script>
    import { BeakerIcon } from '@heroicons/vue/20/solid';
    import Multiselect from '@vueform/multiselect';
    import { useAuthStore } from '@/stores/auth';

    export default {
        components: { Multiselect, BeakerIcon },
        data () {
          return {
            type: null,
            options: [
                'Analgesics', 
                'Antibiotics', 
                'Antivirals',
                'Antifungals',
                'Antacids',
                'Antihistamines',
                'Cardiovascular',
                'Endocrine',
                'Psychotropics',
                'Vaccines',
                'Anti-inflammatory',
                'Dermatological',
                'Gastrointestinal',
                'Respiratory',
                'other',
            ],
            admin: null,
            selections: [
                'oral',
                'parenteral',
                'rectal',
                'vaginal',
                'urethral',
                'intra respiratory',
                'sublingual',
                'intranasal',
                'intra ocular',
                'conjuntival',
                'transdermal',
            ],
            form: null,
            dosage: [
                'tablet',
                'capsules',
                'powder',
                'cream',
                'paste',
                'gel',
                'suppositories',
                'syrup',
                'solution',
                'emulsion',
                'suspension',
                'inhaler',
                'aerosols',
            ],
            openModal: false,
            alert: {visible: false, message: ''},
            name: '',
            batch: '',
            expiry: '',
            qty: '',
            mfcg: '',
            supplier: '',
            strength: '',
            cost: '',
            price: '',
          }
        },
        methods: {
            showAlert(message) {
                alert.value = { visible: true, message };
                setTimeout(() => {
                    alert.value.visible = false;
                }, 3000); 
            },

            async addMedicineData () {
              if (this.type != null && this.admin != null && this.form != null) {
                const authStore = useAuthStore();
                console.log(this.type);
                try {
                  const response =  await fetch('http://127.0.0.1:8000/medicine/add-medicine', {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        'Authorization': `Bearer ${authStore.getAccessToken}`,
                    },
                    body: JSON.stringify({
                        "name": this.name,
                        "batch_number": this.batch,
                        "expiry_date": this.expiry,
                        "quantity": this.qty,
                        "cost": this.cost,
                        "price": this.price,
                        "type": this.type,
                        "administration": this.admin,
                        "strength": this.strength,
                        "manufacturer": this.mfcg,
                        "supplier": this.supplier,
                    })
                  });
                  if (!response.ok) {
                    const errorData = await response.json();
                    this.showAlert(errorData.error);
                  }

                  const success = await response.json();
                  this.showAlert(success.message);
                  this.openModal = false;
                  this.reset();
                } catch (error) {
                    console.error(error);
                    throw error; 
                }          
              } 
            },

            reset() {
              this.type = null;
              this.admin = null;
              this.form = null;
              this.alert = {visible: false, message: ''};
              this.name = '';
              this.batch = '';
              this.expiry = '';
              this.qty = '';
              this.mcfg = '';
              this.supplier = '';
              this.strength = '';
              this.cost = '';
              this.price = '';
            }
        }
    }

    
</script>

<style src="@vueform/multiselect/themes/default.css"></style>