import { useEffect, useState } from 'react';
import { supabase } from '../supabaseClient'

function DisplayTable() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  async function fetchData() {
    const { data, error } = await supabase
      .from('coordinates')
      .select('*');

    if (error) {
      console.error('Error fetching data:', error);
    } else {
      console.log(data)
      setData(data);
    }
  }

  return (
    <table>
      <thead>
        <tr>
          <th>Column 1</th>
          <th>Column 2</th>
          {/* Add more table headers based on your table schema */}
        </tr>
      </thead>
      <tbody>
        {data.map((row) => (
          <tr key={row.id}>
            <td>{row.column1}</td>
            <td>{row.column2}</td>
            {/* Add more table cells based on your table schema */}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default DisplayTable;