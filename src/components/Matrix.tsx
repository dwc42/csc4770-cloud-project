import React from "react";
export default function Matrix({ matrix }: { matrix: number[][]; }) {
	const nRowLength = matrix?.length;
	const mRowLength = matrix[0]?.length;
	if (!nRowLength || !mRowLength) return <p>Invalid Matrix</p>;
	return (
		<div style={{ padding: '20px' }}>
			<h2>User List</h2>

			{/* 2. The HTML Table Structure */}
			<table style={{ width: '100%', borderCollapse: 'collapse', border: '1px solid #ddd' }}>
				<thead>
					<tr style={{ backgroundColor: '#f2f2f2', textAlign: 'left' }}>
						{
							Array(mRowLength + 1).map((_, i) => {
								return <th style={{ padding: '12px' }}>i</th>;
							})
						}

					</tr>
				</thead>
				<tbody>
					{/* 3. Mapping over the data to create rows dynamically */}
					{Array(nRowLength + 1).map((_, n) => {
						return <tr key={n} style={{ borderBottom: '1px solid #ddd' }}>
							{
								Array(mRowLength + 1).map((_, m) => {
									return <td style={{ padding: '12px' }}>{(!m) ? n : matrix[n - 1][m - 1]}</td>;
								})
							}
						</tr>;
					}
					)}
				</tbody>
			</table>
		</div>
	);
} 