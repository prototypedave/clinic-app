<template>
    <div v-if="alert.visible" class="fixed top-4 right-4 bg-green-500 text-white p-4 rounded-md shadow-lg z-50">
        {{ alert.message }}
    </div>
	<div v-if="openTreatment" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      	<div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">        
        	<h2 class="text-xl font-bold mb-4 text-center"> Treatment Plan Form </h2>
        	<form @submit.prevent="getPlan" class="flex flex-col gap-4">
          		<div class='w-full'>
                	<label for="diagnosis" class="block text-sm text-left mb-2 font-medium">Diagnosis*</label>
                	<textarea v-model="diagnosis" class="mt-1 pl-2 block w-full text-sm py-2 bg-violet-200 focus:border-violet-950 rounded-md shadow-sm" required/>
              	</div>
        		<div class='w-full'>
            		<label for="plan" class="block text-sm text-left mb-2 font-medium ">Treatment Plan*</label>
            		<textarea v-model="plan" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm" required/>
                </div>
                <div class="flex gap-4">
                    <input v-model="add" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm" placeholder="Add medicine" />
                    <input v-model="qty" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm" placeholder="Quantity" />
                    <button @click="addMedicine" type="button" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
                </div>
	            <div class="flex justify-end gap-4 h-10">
		            <button @click="openModal = true; openPatientInfo = false" type="button" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md focus:ring focus:ring-secondary-btn-fcs">back</button>
		            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
		        </div>
        	</form>
      	</div>
    </div>
</template>

<script setup>
	import { ref } from 'vue';
    import { useAuthStore } from '@/stores/auth';
    import { usePatientModalStore } from '@/stores/patientModal';
    import { computed } from 'vue';

    const authStore = useAuthStore();
    const modalStore = usePatientModalStore();
    const openTreatment = computed(() => modalStore.getTreatmentPlan);

    const diagnosis = ref('');
    const plan = ref('');
    const medication = ref([]);
    const add = ref('');
    const qty = ref('');
    
    const alert = ref({ visible: false, message: '' });
    const error = ref("");
    
    function showAlert(message) {
        alert.value = { visible: true, message };
        setTimeout(() => {
          alert.value.visible = false;
        }, 3000); 
    };

    async function addMedicine () {
        const backend = "patient/get-medicine";
        if (add.value) {
            const body = JSON.stringify({
                "medicine" : add.value,
            });
        }

        const medicineData = await authStore.APICall({ body: body, api: backend });
        if (medicineData.success) {
            medication.value.push({
                'name': medicineData.data.name,
                'price': medicineData.data.price,
                'qty': qty.value,
            });
            add.value = '';
            qty.value = '';
        } else {
            showAlert(medicineData.data.error);
        }
    }

    async function getRehabData () {
        const backend = "patient/plan-record";

        if (plan.value && diagnosis.value) { 
            const body = JSON.stringify({
                "plan": plan.value,
                "diagnosis": diagnosis.value,
                "medication": medication.value,
                "id" : modalStore.getId
            });

            // poll backend
            const msg = await authStore.APICall({ body: body, api: backend });
            if (msg.success) {
                showAlert(msg.data.message);
                setTimeout(() => {
                    modalStore.reset();
                    //modalStore.prenatalTestModal();
                }, 3000 );              
            } else {
                showAlert(msg.data.error);
            }
        }
    }

</script>