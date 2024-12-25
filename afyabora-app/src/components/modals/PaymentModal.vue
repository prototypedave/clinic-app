<template>
    <div 
        v-if="alert.visible" 
        class="fixed top-4 right-4 bg-green-500 text-white p-4 rounded-md shadow-lg z-50">
        {{ alert.message }}
    </div>
    <button class="flex flex-col p-4 bg-violet-800 justify-between items-center text-white hover:bg-violet-950 rounded-md" @click="openModal = true">
        <CurrencyDollarIcon class="justify-center size-8" aria-hidden="true" />
        <p>Payment</p>
    </button>
    <div v-if="openModal" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
        <div class="bg-violet-300 text-violet-950 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow">
            <h2 class="text-xl font-bold mb-4 text-center">Patient Payment Form</h2>
            <form @submit.prevent="submitNote" class="flex flex-col text-violet-950 gap-4">
                <div class="flex flex-row gap-4">
                    <div>
                        <label for="firstName" class="block text-sm text-left mb-2 font-medium">First Name</label>
                        <input id="firstName" v-model="firstName" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required placeholder='First Name'/>
                    </div>
                    <div>
                        <label for="lastName" class="block text-sm text-left mb-2 font-medium">Last Name</label>
                        <input id="lastName" v-model="secondName" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required placeholder='Last Name'/>
                    </div>
                    <div>
                        <label for="id" class="block text-sm text-left mb-2 font-medium">Patient Id</label>
                        <input id="id" v-model="id" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required placeholder='123456'/>
                    </div>
                </div>
                <div class="flex flex-row gap-4">
                    <div>
                        <label for="invoice" class="block text-sm text-left mb-2 font-medium">Invoice Id</label>
                        <input id="invoice" v-model="invoice" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required placeholder='Invoice Id'/>
                    </div>
                    <div>
                        <label for="amount" class="block text-sm text-left mb-2 font-medium">Amount</label>
                        <input id="amount" v-model="amount" type="number" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required placeholder='Amount paid'/>
                    </div>
                    <div>
                        <label for="date" class="block text-sm text-left mb-2 font-medium">Payment Date</label>
                        <input id="date" v-model="date" type="date" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" required/>
                    </div>
                </div>

                <div class="mt-6 flex gap-2 justify-center">
                    <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">submit</button>  
                    <button @click="openModal = false" class="bg-violet-800 hover:violet-950 text-white font-bold py-2 px-4 rounded-md">close</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
    import { CurrencyDollarIcon } from '@heroicons/vue/20/solid';
    import { ref } from 'vue';

    const openModal = ref(false);
    const alert = ref({ visible: false, message: '' });

    const firstName = ref('');
    const lastName = ref('');
    const id = ref('');
    const invoice = ref('');
    const amount = ref('');
    const date = ref('');
    
    function showAlert(message) {
        alert.value = { visible: true, message };
        setTimeout(() => {
            alert.value.visible = false;
        }, 3000); 
    }

    function submitNote() {
        if (id.value ) {
            showAlert('Payment updated successfully');
            openModal.value = false;
            resetForm();
        }
    }

    function resetForm() {
        firstName.value = '';
        lastName.value = '';
        id.value = '';
        invoice.value = '';
        amount.value = '';
        date.value = '';
    }
</script>