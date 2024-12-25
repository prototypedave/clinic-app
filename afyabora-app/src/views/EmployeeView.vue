<template>
    <div class="flex flex-row text-white max-h-screen">
        <SideBar />
        <div class="flex-1 mx-auto max-w-7xl">
            <h2 class='font-bold m-4 text-indigo-800'>Employees</h2>
            <div class="bg-violet-800 h-12 m-4 rounded-md text-base flex justify-between px-8 text-white">
                <button>New Employee</button>
                <button>Search Employee</button>
                <button>Active Employees</button>
                <button>Inactive Employees</button>
            </div>
            <section class="grid grid-cols-3 gap-4 mb-6 m-4">
                <div class="bg-violet-800 p-4 shadow-md rounded-md">
                    <h3 class="text-lg font-semibold text-indigo-100">Active Employees</h3>
                    <p class="text-2xl font-bold text-violet-200">1/1</p>
                </div>
                <div class="bg-violet-800 p-4 shadow-md rounded-md">
                    <h3 class="text-lg font-semibold text-indigo-100">Inactive Employees</h3>
                    <p class="text-2xl font-bold text-violet-200">0/1</p>
                </div>
                <div class="bg-violet-800 p-4 shadow-md rounded-md">
                    <h3 class="text-lg font-semibold text-indigo-100">Roles Assigned</h3>
                    <p class="text-2xl font-bold text-violet-200">2/2</p>
                </div>
            </section>
            <section class="shadow-md rounded-md m-4">
                <h2 class="text-xl font-bold text-indigo-600 mb-4">Employee List</h2>
                <table class="w-full text-sm text-left rtl:text-right">
                    <thead class="text-sm text-white uppercase bg-violet-800">
                        <tr>
                        <th v-for="(header, index) in tableHeaders" :key="index" class="px-6 py-3">{{ header }}</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr 
                            v-for="(row, index) in tableData" 
                            :key="index" 
                            class="odd:bg-violet-600 odd:text-white even:bg-violet-400">
                            <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ row.name }}</td>
                            <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ row.title }}</td>
                            <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ row.status }}</td>
                            <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ row.joinDate }}</td>
                            <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            <span v-html="row.actions"></span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </section>
        </div>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';

export default {
  components: {
    SideBar,
  },
  data() {
    return {
      tableHeaders: ["Name", "title", "Status", "Join Date", "Actions"],
      tableData: [
        {
          name: "John Doe",
          title: "Doctor",
          status: "Active",
          joinDate: "2022-01-01",
          actions: `<button class="bg-indigo-500 hover:bg-indigo-600 text-white py-1 px-3 rounded-md">Edit</button>
                    <button class="bg-red-500 hover:bg-red-600 text-white py-1 px-3 rounded-md">Restrict</button>`,
        },
        {
          name: "Jane Smith",
          title: "nurse",
          status: "Active",
          joinDate: "2023-05-15",
          actions: `<button class="bg-indigo-500 hover:bg-indigo-600 text-white py-1 px-3 rounded-md">Edit</button>
                    <button class="bg-red-500 hover:bg-red-600 text-white py-1 px-3 rounded-md">Restrict</button>`,
        },
        {
          name: "Sam Wilson",
          title: "Intern",
          status: "Inactive",
          joinDate: "2021-09-10",
          actions: `<button class="bg-indigo-500 hover:bg-indigo-600 text-white py-1 px-3 rounded-md">Edit</button>
                    <button class="bg-red-500 hover:bg-red-600 text-white py-1 px-3 rounded-md">Restrict</button>`,
        },
      ],
    };
  },
};
</script>
