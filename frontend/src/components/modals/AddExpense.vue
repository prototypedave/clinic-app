<template>
    <div 
        v-if="alert.visible" 
        class="fixed top-4 right-4 bg-green-500 text-white p-4 rounded-md shadow-lg z-50">
        {{ alert.message }}
    </div>
    <button class="flex flex-col p-4 bg-violet-800 justify-between items-center text-white hover:bg-violet-950 rounded-md" @click="openModal = true">
        <CreditCardIcon class="justify-center size-8" aria-hidden="true" />
        <p>Expense</p>
    </button>

    <!-- Expense Modal -->
    <div v-if="openModal" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
        <div class="bg-violet-200 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">
            <h2 class="text-xl font-bold mb-4 text-center">Expense Report Form</h2>
            <form @submit.prevent="submitExpense" class="flex flex-col gap-4">
                <p class="text-center">Fill all the Details</p>
                <div class="grid grid-cols-1 gap-4">
                    <input id="expensePurpose" v-model="expensePurpose" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm placeholder-violet-950" required placeholder='Reason for spending'/>
                    <input id="expenseDate" v-model="expenseDate" type="date" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm text-violet-950" required />
                    <input id="expenseAmount" v-model="expenseAmount" type="number" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 placeholder-violet-950 rounded-md shadow-sm" required placeholder='Amount spent/ to be spent'/>
                    <textarea id="note" v-model="note" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm placeholder-violet-950 text-dark-gray" rows="3" placeholder="Additional Notes"></textarea>
                </div>
                <div class="flex justify-end gap-2">
                    <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">Submit</button>  
                    <button @click="openModal = false" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">Close</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
    import { CreditCardIcon } from '@heroicons/vue/20/solid';
    import { ref } from 'vue';
    import { useAuthStore } from '@/stores/auth';

    const openModal = ref(false);
    const alert = ref({ visible: false, message: '' });

    const expensePurpose = ref('');
    const expenseAmount = ref('');
    const note = ref('');
    const expenseDate = ref('');

    const authStore = useAuthStore();

    function showAlert(message) {
        alert.value = { visible: true, message };
        setTimeout(() => {
            alert.value.visible = false;
        }, 3000); 
    }

    async function submitExpense() {
        if (expensePurpose.value && expenseAmount.value) {
            try {
                const response = await fetch("http://localhost:8000/expense/add-expense", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        'Authorization': `Bearer ${authStore.getAccessToken}`,
                    },
                    body: JSON.stringify({
                        "purpose": expensePurpose.value,
                        "amount": expenseAmount.value,
                        "notes": note.value,
                        "date": expenseDate.value,
                    })
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    showAlert(errorData.error);
                }

                const success =  await response.json();
                showAlert(success.message);
                openModal.value = false;
                reset();
            } catch (error) {
                console.error(error);
                throw error; 
            }          
        }
    }

    function reset () {
        expensePurpose.value = '';
        expenseAmount.value = '';
        expenseDate.value = '';
        note.value = '';
    }
</script>