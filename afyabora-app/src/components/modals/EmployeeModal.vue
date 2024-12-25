<template>
    <div v-if="alert.visible" class="fixed top-4 right-4 bg-green-500 text-white p-4 rounded-md shadow-lg z-50">
        {{ alert.message }}
    </div>
    <button class="flex flex-col p-4 bg-violet-800 justify-between items-center text-white hover:bg-violet-950 rounded-md" @click="openModal = true">
        <UserGroupIcon class="justify-center size-8" aria-hidden="true" />
        <p>Employee</p>
    </button>

    <div v-if="openModal" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-4xl shadow text-violet-950">   
        <h2 class="text-xl font-bold mb-4 text-center">Add New Staff</h2>
        <form @submit.prevent="submitMedicine">
          <div class="grid grid-cols-3 gap-4">
            <div>
              <label for="firstName" class="block text-sm text-left mb-2 font-medium">First Name</label>
              <input v-model="firstName" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 rounded-md shadow-sm" placeholder='First Name' required />
            </div>
            <div>
              <label for="lastName" class="block text-sm text-left mb-2 font-medium ">Last Name</label>
              <input v-model="lastName" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder='Last Name' required />
            </div>
            <div>
              <label for="id" class="block text-sm text-left mb-2 font-medium ">ID Number</label>
              <input v-model="id" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder='2342345' required />
            </div>
            <div>
              <label for="license" class="block text-sm text-left mb-2 font-medium ">Licence No</label>
              <input v-model="license" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder='Practice license' required />
            </div>
            <div>
              <label for="email" class="block text-sm text-left mb-2 font-medium ">Email</label>
              <input v-model="email" type="email" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder='@mail.com' required />
            </div>
            <div>
              <label for="mobile" class="block text-sm text-left mb-2 font-medium ">Mobile No.</label>
              <input v-model="mobile" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder='+254' required />
            </div>
            <div>
              <label for="title" class="block text-sm text-left mb-2 font-medium ">Title</label>
              <input v-model="title" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder="nurse" required />
            </div>
            <div>
              <label for="role" class="block text-sm text-left mb-2 font-medium ">Role</label>
              <select v-model="role" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " required>
                <option value="full">Full Access</option>
                <option value="add">Patient Add with other access</option>
                <option value="cream">Only Add</option>
              </select>
            </div>
            <div>
              <label for="address" class="block text-sm text-left mb-2 font-medium ">Address</label>
              <input v-model="address" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder="location" required />
            </div>
            <div>
              <label for="qualification" class="block text-sm text-left mb-2 font-medium ">Qualification</label>
              <input v-model="qualification" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm" placeholder='RN' required />
            </div>
            <div>
              <label for="experience" class="block text-sm text-left mb-2 font-medium ">Experience</label>
              <input v-model="experience" type="number" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm" placeholder='0' required />
            </div>
            <div>
              <label for="school" class="block text-sm text-left mb-2 font-medium ">College/Institute</label>
              <input v-model="school" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border border-darker-gray focus:border-violet-950 rounded-md shadow-sm " placeholder="Training institute" required />
            </div>
                     
          </div>
          <div class="flex justify-end gap-2 mt-4">
              <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">submit</button>  
              <button @click="openModal = false" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">close</button>
          </div>
        </form>
      </div>
    </div>
</template>

<script setup>
    import { UserGroupIcon } from '@heroicons/vue/20/solid';
    import { ref } from 'vue';

    const openModal = ref(false);
    const alert = ref({ visible: false, message: '' });

    const medicineName = ref('');
    const manufacturer = ref('');
    const dosage = ref('');
    const category = ref('');
    const strength = ref('');
    const quantity = ref('');
    const unit = ref('');
    const expiryDate= ref('');
    const purchaseDate = ref('');
    const price = ref('');
    const supplier = ref('');

    function showAlert(message) {
        alert.value = { visible: true, message };
        setTimeout(() => {
            alert.value.visible = false;
        }, 3000); 
    }

    function submitMedicine() {
        showAlert('Medicine updated successfully!');
        reset();
    }

    function reset() {
        medicineName.value = '';
        manufacturer.value  = '';
        dosage.value  = '';
        category.value  = '';
        quantity.value  = '';
        strength.value = '';
        unit.value = '';
        expiryDate.value = '';
        purchaseDate.value = '';
        price.value = '';
        supplier.value = '';
    }
</script>
