<template>
    <div 
        v-if="alert.visible" 
        class="fixed top-4 right-4 bg-green-500 text-white p-4 rounded-md shadow-lg z-50">
        {{ alert.message }}
    </div>
    <button class="flex flex-col p-4 bg-violet-800 justify-between items-center text-white hover:bg-violet-950 rounded-md" @click="openModal = true">
        <UserIcon class="justify-center size-8" aria-hidden="true" />
        <p>Patient</p>
    </button>
    
    <!-- check patient -->
    <div v-if="openModal" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-xl shadow text-violet-950">        
        
        <!-- Patient Look Up -->
        <h2 class="text-xl font-bold mb-1 text-center"> Patient Info Form </h2>
        <p class="text-center text-violet-500 text-sm mb-4"> Enter patient details to continue </p>
        <form @submit.prevent="CheckPatient" class="flex flex-col gap-4">
          <div class="flex gap-4">
            <div>
              <label for="firstName" class="block text-sm text-left mb-2 font-medium">First Name*</label>
              <input v-model="firstName" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='First Name' required />
            </div>
            <div>
              <label for="middleName" class="block text-sm text-left mb-2 font-medium ">Middle Name</label>
              <input v-model="middleName" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " />
            </div>
            <div>
              <label for="lastName" class="block text-sm text-left mb-2 font-medium ">Last Name*</label>
              <input v-model="lastName" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Last Name' required />
            </div>
          </div>
          <div class="flex gap-4">
            <div>
              <label for="patientId" class="block text-sm text-left mb-2 font-medium ">Patient Id*</label>
              <input v-model="patientId" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='1234567' required />
            </div>
            <div>
              <label for="reason" class="block text-sm text-left mb-2 font-medium ">Reason for visit*</label>
              <select v-model="reason" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required>
                <option value="checkup">Check-Up</option>
                <option value="consultation">Consultation</option>
                <option value="emergency">Emergency</option>
                <option value="followup">Follow-Up</option>
              </select> 
            </div>
          </div>
          <div class="flex justify-end gap-4">
            <button @click="openModal = false" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">close</button>
            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Patient Symptoms -->
    <div v-if="openPatientSymptoms" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">        
        <h2 class="text-xl font-bold mb-1 text-center"> Patient Symptoms Data </h2>
        <p class="text-center text-sm mb-4 text-violet-500"> Please fill in all the required fields * </p>
        <form @submit.prevent="getSymptoms" class="flex flex-col gap-4">
          <div class="flex gap-4">
            <div class='w-full'>
              <label for="complaint" class="block text-sm text-left mb-2 font-medium ">Chief Complaint*</label>
              <textarea v-model="complaint" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 bg-violet-200 rounded-md shadow-sm " placeholder='Main concern or reason for the visit' required />
            </div>
          </div>
          <div class="flex gap-4">
            <div class='w-full'>
              <label for="onset" class="block text-sm text-left mb-2 font-medium ">Onset*</label>
              <input v-model="onset" type="date" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " :max="today" required />
            </div>
            <div class='w-full'>
              <label for="duration" class="block text-sm text-left mb-2 font-medium ">Duration*</label>
              <select v-model="duration" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required>
                <option value="hours">Hours</option>
                <option value="days">Days</option>
                <option value="weeks">Weeks</option>
              </select>
            </div>
            <div class='w-full'>
              <label for="frequency" class="block text-sm text-left mb-2 font-medium ">Frequency*</label>
              <select v-model="frequency" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required>
                <option value="constantly">Constant</option>
                <option value="intermittently">Intermittent</option>
                <option value="occasionally">Occosional</option>
              </select>
            </div>
          </div>
          <div class="flex gap-4">
            <div class='w-full'>
              <label for="severity" class="block text-sm text-left mb-2 font-medium ">Severity*</label>
              <select v-model="severity" type="date" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required>
                <option value="mild">Mild</option>
                <option value="moderate">Moderate</option>
                <option value="severe">Severe</option>
              </select>
            </div>
            <div class='w-full'>
              <label for="location" class="block text-sm text-left mb-2 font-medium ">Location*</label>
              <input v-model="location" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder="symptom location" required/>
            </div>
            <div class='w-full'>
              <label for="symptomType" class="block text-sm text-left mb-2 font-medium ">Type of Symptom*</label>
              <input v-model="symptomType" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder="pain" required />
            </div>
          </div>
          <div class="flex gap-4">
            <div class='w-full'>
              <label for="otherSymptoms" class="block text-sm text-left mb-2 font-medium ">Other Symptoms</label>
              <textarea v-model="otherSymptoms" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Other Symptoms'/>
            </div>
          </div>
          <div class="flex justify-end gap-4">
            <button type="button" @click="openModal = true; openPatientSymptoms = false" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">back</button>
            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Review of System -->
    <div v-if="openReview" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-full shadow text-violet-950">        
        <h2 class="text-xl font-bold mb-1 text-center"> Review Of Client </h2>
        <p class="text-center mb-4 text-violet-500"> Note down all reviews patient has </p>
        <form @submit.prevent="getReviewSystem" class="grid grid-cols-2 gap-4">
          <div class="flex flex-col gap-4 p-4">
            <div class='flex flex-row gap-4 '>
              <div class='flex w-full gap-4'>
                <label for="general" class="block text-sm text-left mb-2 font-medium ">General</label>
                <textarea v-model="general" type="text" class="mt-1 ml-20 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
              <div class='flex w-full gap-4'>
                <label for="revCardiovascular" class="block text-sm text-left mb-2 font-medium ">Cardiovascular</label>
                <textarea v-model="revCardiovascular" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
            </div>
            <div class='flex flex-row gap-4'>
              <div class='flex w-full gap-4'>
                <label for="gastrointestinal" class="block text-sm text-left mb-2 font-medium ">Gastrointestinal</label>
                <textarea v-model="gastrointestinal" type="text" class="mt-1 ml-8 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
              <div class='flex w-full gap-4'>
                <label for="revRespiratory" class="block text-sm text-left mb-2 font-medium ">Respiratory</label>
                <textarea v-model="revRespiratory" type="text" class="mt-1 ml-6 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
            </div>
          </div>
          <div class="flex flex-col gap-4 p-4">
            <div class='flex flex-row gap-4'>
              <div class='flex w-full gap-4'>
                <label for="genitourinary" class="block text-sm text-left mb-2 font-medium ">Genitourinary</label>
                <textarea v-model="genitourinary" type="text" class="mt-1 ml-8 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
              <div class='flex w-full gap-4'>
                <label for="revMusculoskeletal" class="block text-sm text-left mb-2 font-medium ">Musculoskeletal</label>
                <textarea v-model="revMusculoskeletal" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
            </div>
            <div class='flex flex-row gap-4'>
              <div class='flex w-full gap-4'>
                <label for="revNeurological" class="block text-sm text-left mb-2 font-medium ">Neurological</label>
                <textarea v-model="revNeurological" type="text" class="mt-1 ml-10 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
              <div class='flex w-full gap-4'>
                <label for="psychiatric" class="block text-sm text-left mb-2 font-medium ">Psychiatric</label>
                <textarea v-model="psychiatric" type="text" class="mt-1 ml-8 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
            </div>
          </div>
          <div class="col-span-2 flex justify-end gap-4 mt-2">
            <button type="button" @click="navigateBack(); openReview = false" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">back</button>
            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Physical Exam -->
    <div v-if="openPhysical" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-full shadow text-violet-950">        
        <h2 class="text-xl font-bold mb-1 text-center"> Physical Exam </h2>
        <p class="text-center text-violet-500 text-sm mb-4"> Check all the test done </p>
        <form @submit.prevent="getPhysicalExam" class="grid grid-cols-2 gap-4 placeholder-violet-950">
          <div class='flex flex-col gap-4'>
            <div>
              <h3 class="text-base font-semibold mb-1 text-violet-600 text-center"> Vital Signs </h3>
              <div class="flex flex-col gap-4 rounded-md p-4">
                <div class="flex flex-row gap-4">
                  <div class='flex gap-4'>
                    <input v-model="temperature" type="number" class="mt-1 pl-2 block text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950 w-full h-8" placeholder="temperature" required />
                    <input v-model="bloodPressure" type="text" class="mt-1 pl-2 block text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950 w-full h-8" placeholder="blood pressure" required />                  
                    <input v-model="heartRate" type="number" class="mt-1 pl-2 block text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950 w-full h-8" placeholder="heart rate" required />
                    <input v-model="respiratoryRate" type="number" class="mt-1 pl-2 block text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950 w-full h-8" placeholder="respiratory rate" required />
                  </div>
                </div>
              </div>
              <div v-if="vitalValidStatus" class="mt-1">
                <p class="text-left text-red-500 pl-2" v-for="(item, index) in vitalErrorMsgs" :key="index">{{ item }}</p>
              </div>
            </div>
            <h3 class="text-base font-semibold mb-1 text-violet-600 text-center"> HEENT Examination </h3>
            <div class='flex flex-col gap-4 rounded-md p-4'>
              <div class='flex flex-row gap-4'>
                <div class='flex w-full gap-4'>
                  <textarea v-model="head" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950" placeholder="head" rows='2'/>
                  <textarea v-model="eyes" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950" placeholder="eyes" rows='2'/>
                </div>
              </div>
              <div class='flex flex-row gap-4'>
                <div class='flex w-full gap-4'>
                  <textarea v-model="nose" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950" placeholder="nose" rows='2'/>
                  <textarea v-model="throat" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950" placeholder="throat" rows='2'/>
                </div> 
              </div>
            </div>
          </div>
          <div class='flex flex-col gap-4'>
            <div>
              <h3 class="text-base font-semibold mb-1 text-violet-600 text-center"> Other Examination </h3>
              <div class='flex flex-col gap-4 rounded-md p-4'>
                <div class='flex flex-row gap-4'>
                  <div class='flex w-full gap-4'>
                    <textarea v-model="abdominal" type="text" class="mt-1 placeholder-violet-950 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " placeholder="Abdominal" rows='3'/>
                    <textarea v-model="cardiovascular" type="text" class="mt-1 pl-2 placeholder-violet-950 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " placeholder="Cardiovascular" rows='3'/>
                  </div>
                </div>
                <div class='flex flex-row gap-4'>
                  <div class='flex w-full gap-4'>
                    <textarea v-model="musculoskeletal" type="text" class="mt-1 pl-2 placeholder-violet-950 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " placeholder="Musculoskeletal" rows='3'/>
                    <textarea v-model="neurological" type="text" class="mt-1 pl-2 block placeholder-violet-950 w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " placeholder="Neurological" rows='3'/>
                  </div>
                </div>
                <div class='flex flex-row gap-4'>
                  <div class='flex w-full gap-4'>
                    <textarea v-model="respiratory" type="text" class="mt-1 pl-2 block placeholder-violet-950 w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " placeholder="Respiratory" rows='3'/>
                    <textarea v-model="skin" type="text" class="mt-1 pl-2 block w-full placeholder-violet-950 text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " placeholder="Skin" rows='3'/>
                  </div>
                </div>
              </div>
            </div> 
          <div class="flex justify-end gap-4 mt-2">
            <button type="button" @click="openReview = true; openPhysical = false" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">back</button>
            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
          </div>
        </div>
        </form>
      </div>
    </div>

    <!-- Lab Results -->
    <div v-if="openLabResult" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">        
        <h2 class="text-xl font-bold mb-4 text-center"> Lab Test Results </h2>
        <form @submit.prevent="fillLabResults" class="flex flex-col gap-4">
          <div class="grid grid-cols-2 gap-4 rounded-md p-4">
            <div class="flex flex-col gap-4">
              <div>
                <label for="testName" class="block text-sm text-left mb-2 font-medium ">Test Name</label>
                <input v-model="testName" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " placeholder='Enter test conducted' />
              </div>
              <div>
                <label for="testResult" class="block text-sm text-left mb-2 font-medium ">Test Results</label>
                <textarea v-model="testResult" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " rows='3'/>
              </div>
              <div>
                <label for="referenceRange" class="block text-sm text-left mb-2 font-medium ">Reference Range</label>
                <textarea v-model="referenceRange" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " rows='3'/>
              </div>
            </div>
            <div class="flex flex-col gap-4">
              <div>
                <label for="interpretation" class="block text-sm text-left mb-2 font-medium ">Interpretation</label>
                <textarea v-model="interpretation" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md  " rows='4'/>
              </div>
              <div>
                <label for="followup" class="block text-sm text-left mb-2 font-medium ">Follow Up</label>
                <textarea v-model="followup" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " rows='4'/>
              </div>
            </div>
            <div class="flex justify-center gap-4 col-span-2">
              <button @click="addResults" type="button" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">Add Another Test</button>
            </div>
          </div>
          <div class="flex justify-end gap-4">
            <button @click="openPhysical = true; openLabResult = false" type="button" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">back</button>
            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Diagnosis -->
    <div v-if="openDiagnosis" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">        
        <h2 class="text-xl font-bold mb-4 text-center"> Diagniosis And Treatment Plan </h2>
        <form @submit.prevent="fillTreatmentPlan" class="flex flex-col gap-4">
          <div class="flex flex-row gap-4">
            <label for="diagnosis" class="block text-sm text-left mb-2 font-medium ">Diagniosis*</label>
            <textarea v-model="diagnosis" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " required rows='3'/>
          </div>
          <div class="flex flex-row gap-4">
            <label for="treatment" class="block text-sm text-left mb-2 font-medium ">Treatment Plan*</label>
            <textarea v-model="treatment" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " required rows='4'/>
          </div>
          <div class="flex flex-row content-center">
            <div class="border border-violet-900 h-0 w-full mt-2"/>
            <h4 class="w-full m-0 text-violet-600 text-center"> Prescribed medicine's </h4>
            <div class="border border-violet-900 h-0 w-full mt-2"/>
          </div>
          <div class="flex flex-row gap-4">
            <div class='w-full'>
              <div class="flex w-full gap-4">
                <div>
                  <label for="medicineName" class="block text-sm text-left mb-2 font-medium ">Medicine Name</label>
                  <input v-model="medicineName" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md "/>
                </div>
                <div class="w-12">
                  <label for="quantity" class="block text-sm text-left mb-2 font-medium ">Qty</label>
                  <input v-model="quantity" type="number" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md text-dark-blue"/>
                </div>
                <button @click="addMedicine" type="button" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md h-[38px] mt-[28px]">add</button>
      
              </div>
              <div v-if="qtyValidStatus" class="mt-4">
                <p class="p-2 text-center rounded text-red-800">
                  Quantity value should be 0 or more
                </p>
              </div>
            </div>
            <div class="w-full">
              <div v-if="added" class='flex flex-col border border-violet-950 rounded-md p-4 h-36 flex-nowrap overflow-auto'>
                <p class="text-form-lb dark: text-left" v-for="(item, index) in medicine" :key="index">{{ item.medicine }}-{{ item.quantity }}</p>
              </div>
            </div>
          </div>
          <div class="flex justify-end gap-4">
            <button @click="openLabResult = true; openDiagnosis = false" type="button" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">back</button>
            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md focus:ring focus:ring-btn-fcs">next</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Invoice -->


    <!-- patient data -->
    <div v-if="openPatientInfo" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">        
        <h2 class="text-xl font-bold mb-4 text-center"> Patient Personal Details </h2>
        <p class="text-center text-violet-500 mb-4"> Please fill in all the required fields * </p>
        <form @submit.prevent="getPatientInfo" class="flex flex-col gap-4">
          <div class="grid grid-rows-4 border border-violet-950 shadow-2xl rounded-md p-4 gap-4">
            <div class="flex justify-between">
              <div>
                <label for="dob" class="block text-sm text-left mb-2 font-medium ">Date of Birth*</label>
                <input v-model="dob" type="date" class="mt-1 pl-2 block w-full text-sm py-2 bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='First Name' required />
              </div>
              <div>
                <label for="age" class="block text-sm text-left mb-2 font-medium ">Age*</label>
                <input v-model="age" type="number" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='0' required />
              </div>
              <div>
                <label for="gender" class="block text-sm text-left mb-2 font-medium ">Gender*</label>
                <select v-model="gender" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='First Name' required >
                  <option value='male'>Male</option>
                  <option value='female'>Female</option>
                </select>
              </div>
            </div>
            <div class="flex justify-between gap-4">
              <div>
                <label for="address" class="block text-sm text-left mb-2 font-medium ">Address</label>
                <input v-model="address" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Kangemi'/>
              </div>
              <div>
                <label for="mobile" class="block text-sm text-left mb-2 font-medium ">Phone Number*</label>
                <input v-model="mobile" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='+254' required />
              </div>
              <div>
                <label for="email" class="block text-sm text-left mb-2 font-medium ">Email*</label>
                <input v-model="email" type="email" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='@company.com' required />
              </div>
            </div>
            <div class="flex flex-col">
              <h4 class="text-center text-violet-600">Emergency Contact </h4>
              <div class="flex justify-between gap-4">
                <div>
                  <label for="emergencyName" class="block text-sm text-left mb-2 font-medium ">Name</label>
                  <input v-model="emergencyName" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Name' />
                </div>
                <div>
                  <label for="relationship" class="block text-sm text-left mb-2 font-medium ">Relationship</label>
                  <input v-model="relationship" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='mum'/>
                </div>
                <div>
                  <label for="phone" class="block text-sm text-left mb-2 font-medium ">Phone</label>
                  <input v-model="phone" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='+254' />
                </div>
              </div>
            </div>
            <div class="flex justify-end gap-4 h-10">
              <button @click="openModal = true; openPatientInfo = false" type="button" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md focus:ring focus:ring-secondary-btn-fcs">back</button>
              <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
          </div>
          </div>
        </form>
      </div>
    </div>

    <!-- medical history -->
    <div v-if="openHistory" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 text-violet-950 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow">        
        <h2 class="text-xl font-bold mb-4 text-center"> Medical History </h2>
        <form @submit.prevent="getHistory" class="grid grid-cols-2 gap-4">
          <div class="flex flex-col gap-4">
            <h4 class="text-center text-violet-600">General Health</h4>
            <div>
              <label for="currentStatus" class="block text-sm text-left mb-2 font-medium ">Current Health</label>
              <textarea v-model="currentStatus" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='1'/>
            </div>
            <div>
              <label for="allergies" class="block text-sm text-left mb-2 font-medium ">Current Health</label>
              <textarea v-model="allergies" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='1'/>
            </div>
            <div>
              <label for="medications" class="block text-sm text-left mb-2 font-medium ">Medications</label>
              <textarea v-model="medications" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='1'/>
            </div>
            <div>
              <label for="surgeries" class="block text-sm text-left mb-2 font-medium ">Surgeries</label>
              <textarea v-model="surgeries" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='1'/>
            </div>
            <div>
              <label for="hospitalization" class="block text-sm text-left mb-2 font-medium ">Hospitalizations</label>
              <textarea v-model="hospitalization" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='1'/>
            </div>
          </div>
          <div class="flex flex-col gap-4">
            <h4 class="text-center text-violet-600">Family History</h4>
            <div>
              <label for="parent" class="block text-sm text-left mb-2 font-medium ">Parent's Health Status</label>
              <textarea v-model="parent" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
            </div>
            <div>
              <label for="sibling" class="block text-sm text-left mb-2 font-medium ">Siblings Health Status</label>
              <textarea v-model="sibling" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
            </div>
          </div> 
          <div class="flex justify-end gap-4 h-10">
              <button @click="openModal = true; openPatientInfo = false" type="button" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">back</button>
          </div>
          <div class="flex justify-start gap-4 h-10">
              <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
          </div> 
        </form>
      </div>
    </div>
</template>

<script setup>
  import { UserIcon } from '@heroicons/vue/20/solid';
  import { ref } from 'vue';

  const openModal = ref(false);
  const alert = ref({ visible: false, message: '' });
  const today = new Date().toISOString().split('T')[0];

  const openPatientInfo = ref(false);
  const openPatientSymptoms = ref(false);
  const openReview = ref(false);
  const openPhysical = ref(false);
  const openLabResult = ref(false);
  const openDiagnosis = ref(false);
  const followUpStatus = ref(false);
  const openHistory = ref(false);

  // check up variables
  const firstName = ref('');
  const middleName = ref('');
  const lastName = ref('');
  const patientId = ref('');
  const reason = ref('');

  // review variables
  const general = ref('');
  const revCardiovascular = ref('');
  const revRespiratory = ref('');
  const gastrointestinal = ref('');
  const genitourinary = ref('');
  const revMusculoskeletal = ref('');
  const revNeurological = ref('');
  const psychiatric = ref('');

  // symptoms variables
  const complaint = ref('');
  const onset = ref('');
  const duration = ref('');
  const frequency = ref('');
  const severity = ref('');
  const location = ref('');
  const symptomType = ref('');
  const otherSymptoms = ref('');

  // exam variables
  const temperature = ref('');
  const bloodPressure = ref('');
  const heartRate = ref('');
  const respiratoryRate = ref('');
  const head = ref('');
  const eyes = ref('');
  const nose = ref('');
  const throat = ref('');
  const cardiovascular = ref('');
  const respiratory = ref('');
  const abdominal = ref('');
  const neurological = ref('');
  const musculoskeletal = ref('');
  const skin = ref('');

  // lab results
  const testName = ref('');
  const testResult = ref('');
  const referenceRange = ref('');
  const interpretation = ref('');
  const followup = ref('');
  const LabResults = ref([]);

  // diagnosis
  const medicine = ref([]);
  const medicineName = ref('');
  const quantity = ref("");
  const added = ref(false);

  // patient info
  const dob = ref('');
  const age = ref('');
  const gender = ref('');
  const address = ref('');
  const mobile = ref('');
  const email = ref('');
  const emergencyName = ref('');
  const relationship = ref('');
  const phone = ref('');

  // validations
  const qtyValidStatus = ref(false);
  const vitalValidStatus = ref(false);
  const vitalErrorMsgs = ref([]);

  function showAlert(message) {
    alert.value = { visible: true, message };
    setTimeout(() => {
      alert.value.visible = false;
    }, 3000); 
  }

  function CheckPatient () {
    if (patientId.value === '123') {
      if (reason.value != 'followup') {
        openModal.value = false;  // close
        openPatientSymptoms.value = true;
      } else {
        openModal.value = false;
        openReview.value = true;
        followUpStatus.value = true;
      }
      
    } else {
      openModal.value = false;
      openPatientInfo.value = true; 
    }
  }

  function getSymptoms () {
    openReview.value = true;
    openModal.value = false;
    openPatientSymptoms.value = false;
  }

  function getReviewSystem () {
    openPhysical.value = true;
    openModal.value = false;
    openPatientSymptoms.value = false;
    openReview.value = false;
  }

  function getPhysicalExam () {
    if (temperature.value < 30 || temperature.value > 42) {
      vitalErrorMsgs.value = [];
      vitalErrorMsgs.value.push('Temperature value out of scale');
      vitalValidStatus.value = true;
    } else if (heartRate.value < 1 ) {
      vitalErrorMsgs.value = [];
      vitalErrorMsgs.value.push('Invalid Heart rate value');
      vitalValidStatus.value = true;
    } else if (respiratoryRate.value < 5 || respiratoryRate.value > 35) {
      vitalErrorMsgs.value = [];
      vitalErrorMsgs.value.push('Respiratory value out of scale');
      vitalValidStatus.value = true;
    } else {
      openPhysical.value = false;
      openModal.value = false;
      openPatientSymptoms.value = false;
      openLabResult.value = true;
      vitalValidStatus.value = false;
      vitalErrorMsgs.value = [];
    }
  }

  function addResults () {
    if (testName.value && testResult.value && referenceRange.value && interpretation.value && followup.value) {
        LabResults.value.push({
          test: testName.value, 
          result: testResult.value, 
          reference: referenceRange.value, 
          interpretation: interpretation.value, 
          followup: followup.value });
        testName.value = '';
        testResult.value = '';
        referenceRange.value = '';
        interpretation.value = '';
        followup.value = '';
        showAlert('Lab Results added');
    } else {
        showAlert('All fields are required!');
    }
  }

  function fillLabResults () {
    if (testName.value && testResult.value && referenceRange.value && interpretation.value && followup.value) {
        LabResults.value.push({
          test: testName.value, 
          result: testResult.value, 
          reference: referenceRange.value, 
          interpretation: interpretation.value, 
          followup: followup.value 
      });
        openPhysical.value = false;
        openModal.value = false;
        openPatientSymptoms.value = false;
        openLabResult.value = false;
        openDiagnosis.value = true;
    } 
        openPhysical.value = false;
        openModal.value = false;
        openPatientSymptoms.value = false;
        openLabResult.value = false;
        openDiagnosis.value = true; 
  }

  function getPatientInfo () {
    openPatientInfo.value  = false;
    openHistory.value = true;
  }

  function getHistory () {
    openHistory.value = false;
    openPatientSymptoms.value = true;
  }

  function addMedicine () {
    if (medicineName.value && quantity.value) {
      if (quantity.value < 1) {
        qtyValidStatus.value = true;
      }
      else {
        medicine.value.push({medicine: medicineName.value, quantity: quantity.value});
        added.value = true;
        medicineName.value = "";
        quantity.value = "";
        qtyValidStatus.value = false;
        showAlert("Medicine added");
      }
    }
  }

  function navigateBack () {
    if (followUpStatus.value) {
      openModal.value = true;
      console.log(openModal.value);
    } else {
      openPatientSymptoms.value = true;
    }
  }

</script>

  <style>
  .disabled {
    background-color: #6c757d;
    cursor: not-allowed;
  }
</style>
